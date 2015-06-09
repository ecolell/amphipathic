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

    @classmethod
    def calculate_index(cls, struct):
        pass

    @classmethod
    def index_secuence(cls, struct):
        struct['index'] = cls.calculate_index(struct)
        print struct

    @classmethod
    def index_secondary(cls, seq, with_power):
        self.with_power = with_power
        map(cls.index_secuence, seq.resume_secondary())


def index(amino_sequence, with_power=False):
    seq = Sequence(amino_sequence)
    seq.resume_secondary()
    Amphipathic.index_secondary(seq, with_power=with_power)
    return seq.resume_secondary()

