# -*- coding: utf-8 -*- #
"""Core Service."""
from __future__ import unicode_literals

import re
import warnings
from Bio import Seq, BiopythonWarning
from math import cos, sin
from amphipathic.services import secondary_structure


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


hydrophobic = {
    'a':  0.22,
    'c':  4.07,
    'd': -3.08,
    'e': -1.81,
    'f':  4.44,
    'g':  0.00,
    'h':  0.46,
    'i':  4.77,
    'k': -3.04,
    'l':  5.66,
    'm':  4.23,
    'n': -0.46,
    'p': -2.23,
    'q': -2.81,
    'r':  1.42,
    's': -0.45,
    't': -1.90,
    'v':  4.67,
    'w':  1.04,
    'y':  3.23
}
FGR = 0.0174533


class Amphipathic(object):

    @classmethod
    def calculate_alpha_index(cls, struct):
        pass

    @classmethod
    def calculate_beta_index(cls, struct):
        pass

    @classmethod
    def apply_func(cls, func, i, h, mean, coefficient):
        return (h - mean) * func((i - 1) * coefficient * FGR)

    @classmethod
    def partial_sum(cls, amph, mean, coefficient):
        sum1 = sum([
            cls.apply_func(cos, i, h, mean, coefficient) for i,h in enumerate(amph)
        ])
        sum2 = sum([
            cls.apply_func(sin, i, h, mean, coefficient) for i, h in enumerate(amph)
        ])
        return sum1 ** 2 + sum2 ** 2

    @classmethod
    def total_sum_norm(cls, h, mean, begin, end, step):
        diff = end - begin
        m1 = 1. / (diff * FGR)
        f1 = ((end * FGR - begin * FGR) / diff * FGR) / 2.  # TODO: Remove FGR
        sumparc1 = cls.partial_sum(h, mean, begin)
        sumparc2 = sum([
            2 * cls.partial_sum(h, mean, angle)
            for angle in range(begin, end, step)
        ])
        sumparc3 = cls.partial_sum(h, mean, end)
        sumtot = sumparc1 + sumparc2 + sumparc3
        return m1 * (f1 * sumtot)

    @classmethod
    def calculate_index(cls, struct):
        angles = {
            'c': (1, 180),
            'e': (100, 160),
            'h': (80, 120),
        }
        seq = struct['seq']
        amount = len(seq) if seq else 1.
        mean = sum([hydrophobic[aa] for aa in seq]) / amount
        h = [hydrophobic[aa] for aa in seq]
        begin, end = angles[struct['type']]
        step = 1  # 1 degree by step
        num = cls.total_sum_norm(h, mean, begin, end, step)
        den = cls.total_sum_norm(h, mean, 1, 180, 1)
        ai = num / (den if den != 0 else 1)
        return ai, mean

    @classmethod
    def index_secuence(cls, struct):
        index, mean = cls.calculate_index(struct)
        struct.update(dict(
            amphipathic=dict(
                index=index,
                mean=mean
            )
        ))
        return struct

    @classmethod
    def index_secondary(cls, seq, with_power):
        cls.with_power = with_power
        [
            [
                cls.index_secuence(aa)
                for aa in protein
            ]
            for protein in seq.resume_secondary()
        ]


def index(sequence, with_power=False):
    seq = Sequence(sequence)
    seq.resume_secondary()
    Amphipathic.index_secondary(seq, with_power=with_power)
    return seq.resume_secondary()

