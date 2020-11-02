# -*- coding: utf-8 -*- #
"""Core Service."""
from __future__ import unicode_literals

import re
import warnings
from math import cos, sin

from Bio import BiopythonWarning, Seq

from amphipathic import secondary_structure, hydrophobic


def is_nucleotide(characters):
    return all([p in ['a', 't', 'c', 'g'] for p in characters])


def obtain_structure(params):
    primary, secondary = params
    structure = []
    elements = [
        m.group(0)
        for m in re.finditer(r"(\w)\1*", secondary)
    ]
    idx = 0
    for e in elements:
        s = {'type': e[0],
             'begin': idx,
             'end': idx + len(e),
             'seq': primary[idx:idx + len(e)]}
        structure.append(s)
        idx += len(e)
    return structure


def apply_secondary_structure(primary):
    return [
        secondary_structure.jpred(seq)
        for seq in primary
    ]


class Sequence(object):

    def __init__(self, string):
        string = string.lower()
        if is_nucleotide(string):
            self.nucleotide = string
            warnings.simplefilter('ignore', BiopythonWarning)
            string = Seq.translate(string).lower()
        self.primary = string.split('*')
        self.secondary = []
        self.structures = []

    def resume_secondary(self):
        if not self.structures:
            self.secondary = apply_secondary_structure(self.primary)
            self.structures = [
                obtain_structure(p)
                for p in zip(self.primary, self.secondary)
            ]
            self.structures = [s for s in self.structures if s]
        return self.structures


FGR = 0.0174533


def apply_func(func, i, h, mean, coefficient):
    return (h - mean) * func(i * coefficient * FGR)


def partial_sum(amph, mean, coefficient):
    sum1 = sum([
        apply_func(cos, i, h, mean, coefficient) for i,h in enumerate(amph)
    ])
    sum2 = sum([
        apply_func(sin, i, h, mean, coefficient) for i, h in enumerate(amph)
    ])
    return sum1 ** 2 + sum2 ** 2


def total_sum_norm(h, mean, begin, end, step):
    diff = end - begin
    m1 = 1. / (diff * FGR)
    f1 = ((end * FGR - begin * FGR) / diff * FGR) / 2.
    sumparc1 = partial_sum(h, mean, begin)
    sumparc2 = sum([
        2 * partial_sum(h, mean, angle)
        for angle in range(begin, end, step)
    ])
    sumparc3 = partial_sum(h, mean, end)
    sumtot = sumparc1 + sumparc2 + sumparc3
    return m1 * (f1 * sumtot)


def calculate_amphipathic_index(struct, **kwargs):
    angles = {
        'c': (1, 180),
        'e': (100, 160),
        'h': (80, 120),
    }
    seq = struct['seq']
    hydrophobic_table = hydrophobic.select_table(**kwargs)
    hydrophobic_scores = [
        hydrophobic_table[aa]
        for aa in seq
        if aa in hydrophobic_table
    ]
    amount = len(hydrophobic_scores)
    amount = amount if amount > 0 else 1.
    mean = sum(hydrophobic_scores) / amount
    begin, end = angles[struct['type']]
    step = 1  # 1 degree by step
    num = total_sum_norm(hydrophobic_scores, mean, begin, end, step)
    den = total_sum_norm(hydrophobic_scores, mean, 1, 180, 1)
    ai = num / (den if den != 0 else 1)
    return ai, mean


def add_indexes_to_secuence(struct, **kwargs):
    index, mean = calculate_amphipathic_index(struct, **kwargs)
    struct.update(dict(
        amphipathic=dict(
            index=index,
            mean=mean
        )
    ))
    return struct


def index_secondary(seq, **kwargs):
    [
        [
            add_indexes_to_secuence(aa, **kwargs)
            for aa in protein
        ]
        for protein in seq.resume_secondary()
    ]


def index(sequence, **kwargs):
    seq = Sequence(sequence)
    seq.resume_secondary()
    index_secondary(seq, **kwargs)
    return seq.resume_secondary()
