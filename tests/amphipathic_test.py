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
        for seq in self.sequences[0:1]:
            print "---"
            resume = amphipathic.index(seq)
            print resume
            # TODO: Should assert Equals to a list of results
