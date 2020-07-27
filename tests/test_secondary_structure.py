# -*- coding: utf-8 -*- #
"""Secondary Structure Services."""
from __future__ import unicode_literals


from amphipathic.secondary_structure import jpred


def test_jpred_1(sequence1):
    result = jpred(sequence1)
    assert result == 'ccceehhhcccccccccccc'