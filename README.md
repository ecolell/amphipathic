amphipathic
===========

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ecolell/amphipathic?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![License](https://img.shields.io/pypi/l/amphipathic.svg)](https://raw.githubusercontent.com/ecolell/amphipathic/master/LICENSE) [![Downloads](https://img.shields.io/pypi/dm/amphipathic.svg)](https://pypi.python.org/pypi/amphipathic/) [![Build Status](https://travis-ci.org/ecolell/amphipathic.svg?branch=master)](https://travis-ci.org/ecolell/amphipathic) [![Coverage Status](https://coveralls.io/repos/ecolell/amphipathic/badge.png)](https://coveralls.io/r/ecolell/amphipathic) [![Code Health](https://landscape.io/github/ecolell/amphipathic/master/landscape.png)](https://landscape.io/github/ecolell/amphipathic/master) [![PyPI version](https://badge.fury.io/py/amphipathic.svg)](http://badge.fury.io/py/amphipathic)
[![Stories in Ready](https://badge.waffle.io/ecolell/amphipathic.png?label=ready&title=Ready)](https://waffle.io/ecolell/amphipathic)

This is a library to evaluate an aminoacid sequence and determine an amphipathic index for each alpha helix or beta sheet.

Requirements
------------

If you want to use this library on any GNU/Linux or OSX system you just need to execute:

    $ pip install noaaclass


If you want to collaborate with this library, you should download the [github repository](https://github.com/ecolell/amphipathic) and execute:

    $ make deploy


Testing
-------

To test all the project you should use the command:

    $ make test


Example
-------

This library can analyze an aminoacid sequence and gives a list of secondary structures with the respective index: 

```python
import amphipathic
resume = amphipathic.index('NLYIQWLKDGGPSSGRPPPS') 
print resume
```

And the result should be:

```python
[[
    {'end': 2,
     'begin': 0,
     'type': u'c',
     'seq': 'nl',
     'amphipathic': {'index': 7.572935321054872e-05, 'mean': 2.6}},
    {'end': 5,
     'begin': 2,
     'type': u'e',
     'seq': 'yiq',
     'amphipathic': {'index': 1.4312912272216411, 'mean': 1.7299999999999998}},
    {'end': 18,
     'begin': 5,
     'type': u'c',
     'seq': 'wlkdggpssgrpp',
     'amphipathic': {'index': 0.002511560979331271, 'mean': -0.43}},
    {'end': 20,
     'begin': 18,
     'type': u'e',
     'seq': 'ps',
     'amphipathic': {'index': 1.6242872515167746, 'mean': -1.34}}
]]
```

It also accept a nucleotide sequence to perform the same analysis:

```python
import amphipathic
resume = amphipathic.index('cgcgtccttggagcaatgcagttcaagaccaagaatcgaattgaacctgt') 
print resume
```

And the output:

```python
[[
    {'end': 12,
     'begin': 0,
     'type': u'c',
     'seq': 'rvlgamqfktkn',
     'amphipathic': {'index': 0.007560225956225585, 'mean': 0.7825000000000001}},
    {'end': 15,
     'begin': 12,
     'type': u'e',
     'seq': 'rie',
     'amphipathic': {'index': 1.6297837670649824, 'mean': 1.4599999999999997}},
    {'end': 16,
     'begin': 15,
     'type': u'c',
     'seq': 'p',
     'amphipathic': {'index': 0.0, 'mean': -2.23}}
]]
```

Questions?
----------

If you want to develope with us or have questions about this library, please file an issue in this repository so some of the project managers can get back to you. Please check the existing (and closed) issues to make sure your issue hasn't already been addressed.
