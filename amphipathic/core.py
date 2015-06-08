import requests
from bs4 import BeautifulSoup


class Sequence(object):

    def __init__(self, string):
        self.primary = string

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
        return ''.join(map(lambda f: f.text, html.select('code font')))

    def secondary_structure(self):
        if not hasattr(self, 'secondary'):
            self.secondary = self.obtain_secondary()
        return self.secondary


class Amphipathic(object):

    def __init__(self, sequence):
        self.sequence = sequence

    def verify(self):
        pass


def index(amino_sequence):
    seq = Sequence(amino_sequence)
    return seq.secondary_structure()
