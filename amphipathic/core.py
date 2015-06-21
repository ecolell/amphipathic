import requests
from bs4 import BeautifulSoup
import re
import warnings
from Bio import Seq, BiopythonWarning


class Sequence(object):

    def __init__(self, string):
        string = string.lower()
        if self.is_nucleotide(string):
            self.nucleotide = string
            warnings.simplefilter('ignore', BiopythonWarning)
            string = Seq.translate(string).lower()
        self.primary = string.split('*')

    def is_nucleotide(self, string):
        return all(map(lambda p: p in ['a', 't', 'c', 'g'], string))

    def obtain_structure(self, params):
        primary, secondary = params
        structure = []
        elements = map(lambda m: m.group(0),
                       re.finditer(r"(\w)\1*", secondary))
        idx = 0
        for e in elements:
            s = {'type': e[0],
                 'begin': idx,
                 'end': idx + len(e),
                 'seq': primary[idx:idx + len(e)]}
            structure.append(s)
            idx += len(e)
        return structure

    def resume_secondary(self):
        if not hasattr(self, 'structure'):
            self.secondary_structure()
            self.structures = map(self.obtain_structure,
                                  zip(self.primary, self.secondary))
            self.structures = filter(lambda s: s, self.structures)
        return self.structures

    def obtain_secondary(self, primary):
        # It uses the GOR4 service to estimate the secondary structure.
        data = {
            'title': '',
            'notice': primary,
            'ali_width': len(primary)
        }
        html = BeautifulSoup(requests.post(
            'https://npsa-prabi.ibcp.fr/cgi-bin/secpred_gor4.pl',
            data).text)
        return ''.join(map(lambda f: f.text,
                           html.select('code font')))

    def secondary_structure(self):
        if not hasattr(self, 'secondary'):
            self.secondary = map(self.obtain_secondary, self.primary)
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

    @classmethod
    def index_secondary(cls, seq, with_power):
        cls.with_power = with_power
        index_protein = lambda protein: map(cls.index_secuence, protein)
        map(index_protein,
            seq.resume_secondary())


def index(sequence, with_power=False):
    seq = Sequence(sequence)
    seq.resume_secondary()
    Amphipathic.index_secondary(seq, with_power=with_power)
    return seq.resume_secondary()

