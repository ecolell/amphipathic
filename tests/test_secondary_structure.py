# -*- coding: utf-8 -*- #
"""Secondary Structure Services."""
from __future__ import unicode_literals


import responses
from amphipathic.secondary_structure import jpred


def test_jpred_1(sequence1):
    responses.add(
        responses.POST,
        "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest/job",
        status=202,
        body=b'<h1>Created JPred job. Interactive access through:</h1><ul><li><a href="http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/chklog?jp_D4o0LnW">http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/chklog?jp_D4o0LnW</a></li></ul>'
    )
    responses.add(
        responses.GET,
        "http://www.compbio.dundee.ac.uk/jpred4/results/jp_D4o0LnW/jp_D4o0LnW.jnet",
        status=200,
        body=b'\njnetpred:-,-,-,E,E,H,H,H,-,-,-,-,-,-,-,-,-,-,-,-,\nJNETCONF:9,9,1,0,0,1,1,0,4,6,7,7,7,7,7,8,8,8,9,9,\nJNETSOL25:-,B,B,B,-,B,B,-,-,-,-,-,-,-,-,-,-,-,-,-,\nJNETSOL5:-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,\nJNETSOL0:-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,\nJNETHMM:-,-,-,E,E,H,H,H,-,-,-,-,-,-,-,-,-,-,-,-,\nJNETPROPE:0.0195,0.0305,0.1357,0.3208,0.3655,0.3012,0.2277,0.1437,0.0886,0.0577,0.0889,0.0735,0.1203,0.0975,0.1058,0.0814,0.0740,0.0715,0.0510,0.0436,\nJNETPROPH:0.0119,0.0206,0.2134,0.2756,0.3422,0.3648,0.3740,0.3656,0.2120,0.1891,0.1242,0.1104,0.0915,0.0835,0.0679,0.0676,0.0505,0.0352,0.0226,0.0171,\nJNETPROPC:0.9631,0.9244,0.3072,0.1311,0.0797,0.1145,0.1908,0.3655,0.6239,0.7646,0.7941,0.8303,0.7729,0.8115,0.8012,0.8361,0.8628,0.8883,0.9241,0.9358,\n'
    )
    result = jpred(sequence1)
    assert result == 'ccceehhhcccccccccccc'