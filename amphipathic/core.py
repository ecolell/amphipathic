import requests
from bs4 import BeautifulSoup
import re


class Sequence(object):

    def __init__(self, string):
        self.primary = string

    def resume_secondary(self):
        if not hasattr(self, 'structure'):
            self.secondary_structure()
            self.structure = []
            elements = map(lambda m: m.group(0),
                           re.finditer(r"(\w)\1*", self.secondary))
            idx = 0
            for e in elements:
                s = {'type': e[0],
                     'begin': idx,
                     'end': idx + len(e),
                     'seq': self.primary[idx:idx + len(e)]}
                self.structure.append(s)
                idx += len(e)
        return self.structure

    def obtain_secondary(self):
        # It uses the GOR4 service to estimate the secondary structure.
        data = {
            'title': '',
            'notice': self.primary,
            'ali_width': len(self.primary)
        }
        html = BeautifulSoup(requests.post(
            'https://npsa-prabi.ibcp.fr/cgi-bin/secpred_gor4.pl',
            data).text)
        self.secondary = ''.join(map(lambda f: f.text,
                                     html.select('code font')))

    def secondary_structure(self):
        if not hasattr(self, 'secondary'):
            self.obtain_secondary()
        return self.secondary


class Amphipathic(object):

    def __init__(self, sequence):
        self.sequence = sequence

    def verify(self):
        pass


def index(amino_sequence):
    seq = Sequence(amino_sequence)
    print seq.secondary_structure()
    return seq.resume_secondary()
