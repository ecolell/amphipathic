import pytest

from amphipathic.hydrophobic import cornette

EXPECTED_SCALES = [
    'zimmr', 'ntan', 'ntanr', 'jones', 'levit', 'hoppw', 'yungd', 'faupl',
    'zaslz', 'wolf', 'kuntz', 'abodr', 'meek', 'buldg', 'eisen', 'kytdo',
    'choth', 'wersc', 'janin', 'olsen', 'meiro', 'ponnu', 'nneig', 'robos',
    'chdlg', 'wsdlg', 'jadlg', 'guy', 'guym', 'kridg', 'krigk', 'nioii',
    'mijer', 'rosef', 'sweet', 'sweig', 'rekkr', 'vhebl', 'fromm', 'eimcl',
    'prift', 'prils', 'altft', 'altls', 'totft', 'totls',
]


def test_get_scales():
    assert cornette.get_scales() == EXPECTED_SCALES


EXPECTED_VALUES = [
    ("1.1", 1.1),
    ("-2.1", -2.1),
    ("N", "N"),
    ("TRUE", True),
    ("FALSE", False),
    ("invalid", "invalid"),
]

@pytest.mark.parametrize("value,expected", EXPECTED_VALUES)
def test_clean(value, expected):
    assert cornette.clean(value) == expected
