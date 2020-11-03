import enum
import csv
from functools import lru_cache
import os
import amphipathic


class UnknownScaleError(Exception):
    pass


@lru_cache(maxsize=None)
def load(filename):
    complete_path = os.path.join(amphipathic.__path__[0], "hydrophobic", "data", filename)
    with open(complete_path, newline='', mode="r") as csvfile:
        reader = csv.reader(csvfile)
        return {
            row[0]: row[1:]
            for row in reader
        }


ACCEPTED_VALUES = {
    "TRUE": True,
    "FALSE": False,
}


def clean(value):
    try:
        return float(value)
    except ValueError:
        return ACCEPTED_VALUES.get(value, value)


@lru_cache(maxsize=None)
def load_file(normalized:bool):
    filename = "cornette"
    if normalized:
        filename += "_normalized"
    filename += ".csv"
    return load(filename)


@lru_cache(maxsize=None)
def load_table(normalized:bool, scale:str):
    db = load_file(normalized)
    headers = [head.lower() for head in db["name"]]
    try:
        values = db[scale.lower()]
    except KeyError:
        raise UnknownScaleError
    live_table = {
        key: clean(value)
        for (key, value) in zip(headers, values)
    }
    return live_table


@lru_cache(maxsize=None)
def get_scales(normalized=True):
    db = load_file(normalized)
    return list(db.keys())[1:]


@lru_cache(maxsize=None)
def select_table(normalized=True, scale="PRIFT"):
    table = load_table(normalized, scale)
    return {
        key: value
        for (key, value) in table.items()
        if len(key) == 1
    }


@lru_cache(maxsize=None)
def get_property(normalized=True, scale="PRIFT", property="experimental"):
    table = load_table(normalized, scale)
    return table[property]


def is_experimental(normalized=True, scale="PRIFT"):
    return get_property(normalized, scale, "experimental")


def is_statistical(normalized=True, scale="PRIFT"):
    return get_property(normalized, scale, "statistic")


def is_average(normalized=True, scale="PRIFT"):
    return get_property(normalized, scale, "average")


def is_owned(normalized=True, scale="PRIFT"):
    return get_property(normalized, scale, "own")
