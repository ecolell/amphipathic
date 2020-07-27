import pytest

@pytest.fixture(name="sequence0")
def fixture_sequence_0():
    return 'NLYIQWLXDGGPSSGRPPPS'


@pytest.fixture(name="sequence1")
def fixture_sequence_1():
    return 'NLYIQWLKDGGPSSGRPPPS'


@pytest.fixture(name="sequence2")
def fixture_sequence_2():
    return 'MALPVTALLLPLALLLHAARPSQFRVSPLDRTWNLGETVELKCQVLLSNPTSGCSWLFQPRGA'


@pytest.fixture(name="sequence3")
def fixture_sequence_3():
    return 'ggctgacggctgggttaagaagtttactgaggcagttaacgcctttaagggtttggactggatc'\
           'cgctgccaagttgtccaagttccttgattggatcaaatccaagatcatcccggagctcagagag'\
           'agagcggagtttgttaagaatcttaggcagcttcctcttctcgaggcccagatcaccactttgg'\
           'agcactccaaccctaatcaggagacccaagaacagcttttctcgaacgtccaatacctggcaca'\
           'ccactgtaggaagaacgctccgctctatgcagcggaagcccggagagttttcgcactagagaaa'
