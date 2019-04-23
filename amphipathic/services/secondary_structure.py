# -*- coding: utf-8 -*- #
"""Secondary Structure Services."""
from __future__ import unicode_literals

import re
import time

import requests
from bs4 import BeautifulSoup
from cachetools.func import ttl_cache


class AmphipathicSecondaryStructureError(Exception):
    pass


@ttl_cache(ttl=10*60)
def gor(seq):
    # It uses the GOR4 service to estimate the secondary structure.
    data = {
        'title': '',
        'notice': seq,
        'ali_width': len(seq)
    }
    html = BeautifulSoup(requests.post(
        'https://npsa-prabi.ibcp.fr/cgi-bin/secpred_gor4.pl',
        data).text, 'html.parser')
    return ''.join([
        f.text
        for f in html.select('code font')
    ])


@ttl_cache(ttl=10*60)
def jpred(seq):
    url = 'http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest/job'
    separator = '£€£€'
    params = [
        'skipPDB=on',
        'format=seq',
        '>query\n' + seq
    ]
    data = separator.join(params)
    headers = {
        #'TE': 'deflate, gzip;q = 0.3',
        #'Connection': 'TE, close',
        'User-Agent': 'libwww-perl/6.38',
        'Content-Type': 'text/txt',
    }
    res = requests.post(
        url,
        data.encode('utf-8'),
        headers=headers
    )
    if res.status_code == 202:
        matches = re.search(
            r'(?:href=[\'"])([:/.A-z?<_&\s=>0-9;-]+)',
            res.content.decode('utf-8')
        )
        if not matches:
            # The services doesn't accept the sequence.
            return 'c' * len(seq)
        job_link = matches.group(1)
        job_id = job_link.split('?')[1]
        url = 'http://www.compbio.dundee.ac.uk/jpred4/results/{job_id}/{job_id}.jnet'.format(job_id=job_id)
        res = requests.get(url)
        while res.status_code == 404:
            time.sleep(10)
            res = requests.get(url)
        data = res.content.decode('utf-8')
        return data.split('\n')[1].replace('jnetpred:', '').replace(',', '').lower().replace('-', 'c')
    else:
        raise AmphipathicSecondaryStructureError('We cannot predict the secondary structure')
