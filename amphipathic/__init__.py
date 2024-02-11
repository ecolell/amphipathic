# -*- coding: utf-8 -*- #
"""Core Service."""
from __future__ import unicode_literals

import re
from typing import Any, Callable, Dict, List, Tuple, Union
import warnings
from math import cos, sin

from Bio import BiopythonWarning, Seq

from amphipathic import secondary_structure
from amphipathic.hydrophobic.core import (
    Author,
    select_table as select_hydrophobic_table,
)


def is_nucleotide(characters: str) -> bool:
    return all([p in ['a', 't', 'c', 'g'] for p in characters])


def obtain_structure(params: Tuple[str, str]) -> List[Dict[str, Any]]:
    primary, secondary = params
    structure = []
    elements = [m.group(0) for m in re.finditer(r'(\w)\1*', secondary)]
    idx = 0
    for e in elements:
        s = {
            'type': str(e[0]),
            'begin': int(idx),
            'end': int(idx + len(e)),
            'seq': str(primary[idx : idx + len(e)]),
        }
        structure.append(s)
        idx += len(e)
    return structure


def apply_secondary_structure(primary: List[str]) -> List[str]:
    return [secondary_structure.jpred(seq) for seq in primary]


class Sequence(object):
    def __init__(self, string: str):
        string = string.lower()
        if is_nucleotide(string):
            self.nucleotide = string
            warnings.simplefilter('ignore', BiopythonWarning)
            string = Seq.translate(string).lower()
        self.primary: List[str] = string.split('*')
        self.secondary: List[str] = []
        self.structures: List[List[Dict[str, Any]]] = []

    def resume_secondary(self) -> List[List[Dict[str, Any]]]:
        if not self.structures:
            self.secondary = apply_secondary_structure(self.primary)
            self.structures = [
                obtain_structure(p) for p in zip(self.primary, self.secondary)
            ]
            self.structures = [s for s in self.structures if s]
        return self.structures


FGR = 0.0174533


def apply_func(
    func: Callable[[float | int], float],
    i: int,
    h: float,
    mean: float,
    coefficient: int,
) -> float:
    return (h - mean) * func(i * coefficient * FGR)


def partial_sum(
    amph: List[float], mean: float, coefficient: int
) -> float | int:
    sum1 = sum(
        [apply_func(cos, i, h, mean, coefficient) for i, h in enumerate(amph)]
    )
    sum2 = sum(
        [apply_func(sin, i, h, mean, coefficient) for i, h in enumerate(amph)]
    )
    return sum1**2 + sum2**2


def total_sum_norm(
    h: List[float], mean: float, begin: int, end: int, step: int
) -> float:
    diff = end - begin
    m1 = 1.0 / (diff * FGR)
    f1 = ((end * FGR - begin * FGR) / diff * FGR) / 2.0
    sumparc1 = partial_sum(h, mean, begin)
    sumparc2 = sum(
        [2 * partial_sum(h, mean, angle) for angle in range(begin, end, step)]
    )
    sumparc3 = partial_sum(h, mean, end)
    sumtot = sumparc1 + sumparc2 + sumparc3
    return m1 * (f1 * sumtot)


def calculate_amphipathic_index(
    struct: Dict[str, Any],
    author: Author = Author.CORNETTE,
    normalized: bool = True,
    scale: str = 'PRIFT',
) -> Tuple[float, float]:
    angles = {
        'c': (1, 180),
        'e': (100, 160),
        'h': (80, 120),
    }
    seq = struct['seq']
    hydrophobic_table = select_hydrophobic_table(
        author=author,
        normalized=normalized,
        scale=scale,
    )
    hydrophobic_scores = [
        hydrophobic_table[aa] for aa in seq if aa in hydrophobic_table
    ]
    amount = len(hydrophobic_scores)
    amount = amount if amount > 0 else 1
    mean = sum(hydrophobic_scores) / amount
    begin, end = angles[struct['type']]
    step = 1  # 1 degree by step
    num = total_sum_norm(hydrophobic_scores, mean, begin, end, step)
    den = total_sum_norm(hydrophobic_scores, mean, 1, 180, 1)
    ai = num / (den if den != 0 else 1)
    return ai, mean


def add_indexes_to_secuence(
    struct: Dict[str, Any],
    author: Author = Author.CORNETTE,
    normalized: bool = True,
    scale: str = 'PRIFT',
) -> Dict[str, Any]:
    index, mean = calculate_amphipathic_index(
        struct=struct,
        author=author,
        normalized=normalized,
        scale=scale,
    )
    struct.update(dict(amphipathic=dict(index=index, mean=mean)))
    return struct


def index_secondary(
    seq: Sequence,
    author: Author = Author.CORNETTE,
    normalized: bool = True,
    scale: str = 'PRIFT',
) -> None:
    [
        [
            add_indexes_to_secuence(
                struct=aa,
                author=author,
                normalized=normalized,
                scale=scale,
            )
            for aa in protein
        ]
        for protein in seq.resume_secondary()
    ]


def index(
    sequence: str,
    author: Author = Author.CORNETTE,
    normalized: bool = True,
    scale: str = 'PRIFT',
) -> List[List[Dict[str, Union[str, Any]]]]:
    seq = Sequence(sequence)
    seq.resume_secondary()
    index_secondary(
        seq,
        author=author,
        normalized=normalized,
        scale=scale,
    )
    return seq.resume_secondary()
