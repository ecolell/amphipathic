from __future__ import unicode_literals
from __future__ import print_function
import pytest

import amphipathic


def test_amphipathic_index_1(sequence1):
    resume = amphipathic.index(sequence1)
    for prot in resume:
        for struct in prot:
            assert 'amphipathic' in struct
    seq = [
        [
            s for s in prot
            if s['amphipathic']['index'] > 2.5
        ]
        for prot in resume
    ]
    print("---")
    print(filter(lambda protein: protein, seq))


def test_amphipathic_index_2(sequence2):
    resume = amphipathic.index(sequence2)
    for prot in resume:
        for struct in prot:
            assert 'amphipathic' in struct
    seq = [
        [
            s for s in prot
            if s['amphipathic']['index'] > 2.5
        ]
        for prot in resume
    ]
    print("---")
    print(filter(lambda protein: protein, seq))


def test_amphipathic_index_3(sequence3):
    resume = amphipathic.index(sequence3)
    for prot in resume:
        for struct in prot:
            assert 'amphipathic' in struct
    seq = [
        [
            s for s in prot
            if s['amphipathic']['index'] > 2.5
        ]
        for prot in resume
    ]
    print("---")
    print(filter(lambda protein: protein, seq))
