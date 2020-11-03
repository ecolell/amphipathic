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


EXPECTED_CLEANED_VALUES = [
    ("1.1", 1.1),
    ("-2.1", -2.1),
    ("N", "N"),
    ("TRUE", True),
    ("FALSE", False),
    ("invalid", "invalid"),
]


@pytest.mark.parametrize("value,expected", EXPECTED_CLEANED_VALUES)
def test_clean(value, expected):
    assert cornette.clean(value) == expected


EXPECTED_PROPERTIES_VALUES = [
    (
        cornette.is_experimental,
        True,
        "prift",
        False
    ),
    (
        cornette.is_experimental,
        False,
        "prift",
        False
    ),
    (
        cornette.is_owned,
        True,
        "prift",
        True
    ),
    (
        cornette.is_average,
        True,
        "prift",
        False
    ),
    (
        cornette.is_statistical,
        True,
        "prift",
        True
    ),
    (
        cornette.is_statistical,
        True,
        "ponnu",
        True
    )
]


@pytest.mark.parametrize("property,normalized,scale,expected", EXPECTED_PROPERTIES_VALUES)
def test_properties(property,normalized,scale,expected):
    assert property(normalized=normalized, scale=scale) == expected


def test_load_table_unknown_scale():
    with pytest.raises(cornette.UnknownScaleError):
        cornette.load_table(normalized=True, scale="invalid_one")
