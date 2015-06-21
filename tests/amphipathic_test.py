import unittest
import amphipathic


class TestNoaaclass(unittest.TestCase):

    def setUp(self):
        self.sequences = [
            'NLYIQWLKDGGPSSGRPPPS',
            ('MALPVTALLLPLALLLHAARPSQFRVSPLDRTWNLGETVELKCQVLLSNPTSGCSWLFQPRGA'
             'AASPTFLLYLSQNKPKAAEGLDTQRFSGKRLGDTFVLTLSDFRRENEGCYFCSALSNSIMYFS'
             'HFVPVFLPAKPTTTPAPRPPTPAPTIASQPLSLRPEACRPAAGGAVHTRGLDFACDIYIWAPL'
             'AGTCGVLLLSLVITLYCNHRNRRRVCKCPRPVVKSGDKPSLSARYV'),
            ('ggctgacggctgggttaagaagtttactgaggcagttaacgcctttaagggtttggactggatc'
             'cgctgccaagttgtccaagttccttgattggatcaaatccaagatcatcccggagctcagagag'
             'agagcggagtttgttaagaatcttaggcagcttcctcttctcgaggcccagatcaccactttgg'
             'agcactccaaccctaatcaggagacccaagaacagcttttctcgaacgtccaatacctggcaca'
             'ccactgtaggaagaacgctccgctctatgcagcggaagcccggagagttttcgcactagagaaa'
             'cgcgtccttggagcaatgcagttcaagaccaagaatcgaattgaacctgtttgctgtttgatcc'
             'atggaacgccgggcactggtaaatcacttgccacgactattattggcaggaagatcgctgagta'
             'cgagaatagcggggtctatagtttgccacctgacccagaccactttgatggctacgccgagcag'
             'gcagttgtaattatggatgatctgcatcagaacccagacggcaaagatatgagcttgttttgtc'
             'agatggtttccaccacccccttcgtggttccgatggctgctctcgaggataaaggtagactttt'
             'cacctccaaatatgtgctggcctcaacaaatgccaaccatatccatccagttacagtcgccgat'
             'ggaaaggcccttcagcgccgcttccacttcgacacggacattgaattgatggatggcttcgtga'
             'aaaacgggaaactagatattcagagggcaaccgaggcatgtgaagactgttctccgatcaactt'
             'tcagaagtgcatgcctctcatttgtggtaaggctctccagctccgtagcaagaagggtgatggc'
             'atgagatacagcattgataccatgatcacagagatgcgcagggagtcagcccgacgctataata'
             'ttgggaatgttatagaggcactcttccaa')
        ]

    def test_amphipathic_index(self):
        resume = map(amphipathic.index, self.sequences)
        fil = lambda seq: map(lambda prot:
                              filter(lambda s:
                                     s['amphipathic']['index'] > 2.5,
                                     prot),
                              seq)
        for seq in map(fil, resume):
            print "---"
            print seq
            # TODO: Should assert Equals to a list of results
