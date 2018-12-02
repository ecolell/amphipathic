import pytest
import os
import sys
import json


@pytest.fixture(scope="class")
def load_input():
    def loader(filename):
        path = os.path.dirname(os.path.abspath(__file__))
        with open('{:}/input-samples/{:}'.format(path, filename), 'r') as f:
            data = f.read()
        return unicode(data) if sys.version_info[0] == 2 else data
    return loader


@pytest.fixture(scope="class")
def load_json():
    def loader(filename):
        path = os.path.dirname(os.path.abspath(__file__))
        with open('{:}/input-samples/{:}'.format(path, filename), 'r') as f:
            data = json.load(f)
        return data
    return loader
