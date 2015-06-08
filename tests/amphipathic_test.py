import unittest
import amphipathic


class TestNoaaclass(unittest.TestCase):

    def setUp(self):
        self.sequences = [
            'NLYIQWLKDGGPSSGRPPPS',
            ('MALPVTALLLPLALLLHAARPSQFRVSPLDRTWNLGETVELKCQVLLSNPTSGCSWLFQPRGA'
             'AASPTFLLYLSQNKPKAAEGLDTQRFSGKRLGDTFVLTLSDFRRENEGCYFCSALSNSIMYFS'
             'HFVPVFLPAKPTTTPAPRPPTPAPTIASQPLSLRPEACRPAAGGAVHTRGLDFACDIYIWAPL'
             'AGTCGVLLLSLVITLYCNHRNRRRVCKCPRPVVKSGDKPSLSARYV')
        ]

    def test_amphipathic_index(self):
        for seq in self.sequences:
            index = amphipathic.index(seq)
            print index
            # TODO: Should assert Equals to a list of results
