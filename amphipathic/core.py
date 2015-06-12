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


hidrophobic = {
    'a':  0.22,
    'c':  4.07,
    'd': -3.08,
    'e': -1.81,
    'f':  4.44,
    'g':  0.00,
    'h':  0.46,
    'i':  4.77,
    'k': -3.04,
    'l':  5.66,
    'm':  4.23,
    'n': -0.46,
    'p': -2.23,
    'q': -2.81,
    'r':  1.42,
    's': -0.45,
    't': -1.90,
    'v':  4.67,
    'w':  1.04,
    'y':  3.23
}
FGR = 0.0174533


class Amphipathic(object):

    @classmethod
    def calculate_alpha_index(cls, struct):
        pass

    @classmethod
    def calculate_beta_index(cls, struct):
        pass

    @classmethod
    def calculate_index(cls, struct):
        angles = {
            'e': (100, 160),
            'h': (80, 120),
        }
        step = 1  # 1 degree by step
        pass

    @classmethod
    def index_secuence(cls, struct):
        struct['index'] = cls.calculate_index(struct)
        print struct

    @classmethod
    def index_secondary(cls, seq, with_power):
        # self.with_power = with_power
        map(cls.index_secuence, seq.resume_secondary())


def index(amino_sequence, with_power=False):
    seq = Sequence(amino_sequence)
    seq.resume_secondary()
    Amphipathic.index_secondary(seq, with_power=with_power)
    return seq.resume_secondary()

