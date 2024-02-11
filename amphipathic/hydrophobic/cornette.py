import csv
from functools import lru_cache
import os
from typing import Dict, List, Union
import amphipathic


class UnknownScaleError(Exception):
    pass


@lru_cache(maxsize=None)
def load(filename: str) -> Dict[str, List[str]]:
    complete_path = os.path.join(
        amphipathic.__path__[0], 'hydrophobic', 'data', filename
    )
    with open(complete_path, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        return {row[0]: row[1:] for row in reader}


ACCEPTED_VALUES = {
    'TRUE': True,
    'FALSE': False,
}


def clean(value: str) -> Union[float, bool, str]:
    try:
        return float(value)
    except ValueError:
        return ACCEPTED_VALUES.get(value, value)


@lru_cache(maxsize=None)
def load_file(normalized: bool) -> Dict[str, List[str]]:
    filename = 'cornette'
    if normalized:
        filename += '_normalized'
    filename += '.csv'
    return load(filename)


@lru_cache(maxsize=None)
def load_table(normalized: bool, scale: str) -> Dict[str, float | bool | str]:
    db = load_file(normalized)
    headers = [head.lower() for head in db['name']]
    try:
        values = db[scale.lower()]
    except KeyError:
        raise UnknownScaleError
    live_table = {key: clean(value) for (key, value) in zip(headers, values)}
    return live_table


@lru_cache(maxsize=None)
def get_scales(normalized: bool = True) -> List[str]:
    db = load_file(normalized)
    return list(db.keys())[1:]


@lru_cache(maxsize=None)
def select_table(
    normalized: bool = True, scale: str = 'PRIFT'
) -> Dict[str, float]:
    table = load_table(normalized=normalized, scale=scale)
    return {
        key: value
        for (key, value) in table.items()
        if len(key) == 1 and isinstance(value, float)
    }


@lru_cache(maxsize=None)
def get_property(
    normalized: bool = True,
    scale: str = 'PRIFT',
    property: str = 'experimental',
) -> float | bool | str:
    table = load_table(normalized=normalized, scale=scale)
    return table[property]


def is_experimental(normalized: bool = True, scale: str = 'PRIFT') -> bool:
    value = get_property(
        normalized=normalized, scale=scale, property='experimental'
    )
    if isinstance(value, bool):
        return value
    return False


def is_statistical(normalized: bool = True, scale: str = 'PRIFT') -> bool:
    value = get_property(
        normalized=normalized, scale=scale, property='statistic'
    )
    if isinstance(value, bool):
        return value
    return False


def is_average(normalized: bool = True, scale: str = 'PRIFT') -> bool:
    value = get_property(
        normalized=normalized, scale=scale, property='average'
    )
    if isinstance(value, bool):
        return value
    return False


def is_owned(normalized: bool = True, scale: str = 'PRIFT') -> bool:
    value = get_property(normalized=normalized, scale=scale, property='own')
    if isinstance(value, bool):
        return value
    return False
