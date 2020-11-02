# -*- coding: utf-8 -*- #
"""Secondary Structure Services."""
from __future__ import unicode_literals


import amphipathic


def test_amphipathic_index_0(sequence0, mocker):
    mocker.patch.object(amphipathic, 'apply_secondary_structure')
    amphipathic.apply_secondary_structure.return_value = [
        'ccceehhhcccccccccccc'
    ]
    resume = amphipathic.index(sequence0)
    assert resume[0] == [
        {
            'amphipathic': {'index': 1.0, 'mean': 2.81},
            'begin': 0,
            'end': 3,
            'seq': 'nly',
            'type': 'c'
        },
        {
            'amphipathic': {'index': 1.6242872515167734, 'mean': 0.9799999999999998},
             'begin': 3,
             'end': 5,
             'seq': 'iq',
             'type': 'e'
        },
        {
            'amphipathic': {'index': 1.1841818371579635, 'mean': 3.35},
             'begin': 5,
             'end': 8,
             'seq': 'wlx',
             'type': 'h'
        },
        {
            'amphipathic': {'index': 1.0, 'mean': -0.9941666666666668},
            'begin': 8,
            'end': 20,
            'seq': 'dggpssgrppps',
            'type': 'c'
        }
    ]


def test_amphipathic_index_1(sequence1, mocker):
    mocker.patch.object(amphipathic, 'apply_secondary_structure')
    amphipathic.apply_secondary_structure.return_value = [
        'ccceehhhcccccccccccc'
    ]
    resume = amphipathic.index(sequence1)
    assert resume[0] == [
        {
            'type': 'c',
            'begin': 0,
            'end': 3,
            'seq': 'nly',
            'amphipathic': {'index': 1.0, 'mean': 2.81}
        },
        {
            'type': 'e',
            'begin': 3,
            'end': 5,
            'seq': 'iq',
            'amphipathic': {'index': 1.6242872515167734, 'mean': 0.9799999999999998}
        },
        {
            'type': 'h',
            'begin': 5,
            'end': 8,
            'seq': 'wlk',
            'amphipathic': {'index': 1.155091623405534, 'mean': 1.22}
        },
        {
            'type': 'c',
            'begin': 8,
            'end': 20,
            'seq': 'dggpssgrppps',
            'amphipathic': {'index': 1.0, 'mean': -0.9941666666666668}
        }
    ]


def test_amphipathic_index_2(sequence2, mocker):
    mocker.patch.object(amphipathic, 'apply_secondary_structure')
    amphipathic.apply_secondary_structure.return_value = [
        'ccchhhhhhhhhhhhhhhhccccceeccccccccccceeeeeeeeecccccccceeeeccccc'
    ]
    resume = amphipathic.index(sequence2, scale="prift")
    assert resume[0] == [
        {
            'type': 'c',
            'begin': 0,
            'end': 3,
            'seq': 'mal',
            'amphipathic': {'index': 1.0, 'mean': 3.3699999999999997}
        },
        {
            'type': 'h',
            'begin': 3,
            'end': 19,
            'seq': 'pvtalllplalllhaa',
            'amphipathic': {'index': 0.7203991559243234, 'mean': 2.454375}
        },
        {
            'type': 'c',
            'begin': 19,
            'end': 24,
            'seq': 'rpsqf',
            'amphipathic': {'index': 1.0, 'mean': 0.07400000000000002}
        },
        {
            'type': 'e',
            'begin': 24,
            'end': 26,
            'seq': 'rv',
            'amphipathic': {'index': 1.6242872515167737, 'mean': 3.045}
        },
        {
            'type': 'c',
            'begin': 26,
            'end': 37,
            'seq': 'spldrtwnlge',
            'amphipathic': {'index': 1.0, 'mean': 0.35000000000000003}
        },
        {
            'type': 'e',
            'begin': 37,
            'end': 46,
            'seq': 'tvelkcqvl',
            'amphipathic': {'index': 0.9132957541599984, 'mean': 1.6855555555555555}
        },
        {
            'type': 'c',
            'begin': 46,
            'end': 54,
            'seq': 'lsnptsgc', 'amphipathic': {'index': 1.0, 'mean': 0.53}
        },
        {
            'type': 'e',
            'begin': 54,
            'end': 58,
            'seq': 'swlf',
            'amphipathic': {'index': 0.6423054796591475, 'mean': 2.6725000000000003}
        },
        {
            'type': 'c',
            'begin': 58,
            'end': 63,
            'seq': 'qprga',
            'amphipathic': {'index': 1.0, 'mean': -0.6799999999999999}
        }
    ]


def test_amphipathic_index_3(sequence3, mocker):
    mocker.patch.object(amphipathic, 'apply_secondary_structure')
    amphipathic.apply_secondary_structure.return_value = [
        'c',
        'ccc',
        'ccc',
        'cc',
        'cc',
        'ccccccccccccccccccccccccchhhhhhhhhhhhhhhcccccccccccccccccccccccccccchhhhhhhhhhhccccccccc',
        'c'
    ]
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
