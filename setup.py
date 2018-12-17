#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import os
import subprocess
from setuptools.command import easy_install


__version__ = '0.2.2'


def parse_requirements(filename):
    return [
        line.strip()
        for line in open(filename).readlines()
        if (line.strip())[0] != '#'
    ]


requirements = parse_requirements('requirements.txt')


def get_long_description():
    readme_file = 'README.md'
    if not os.path.isfile(readme_file):
        return ''
    # Try to transform the README from Markdown to reStructuredText.
    try:
        easy_install.main(['-U', 'pyandoc==0.0.1'])
        import pandoc
        pandoc.core.PANDOC_PATH = 'pandoc'
        doc = pandoc.Document()
        doc.markdown = open(readme_file).read()
        description = doc.rst
    except Exception:
        description = open(readme_file).read()
    return description


setup(
    name='amphipathic',
    version=__version__,
    author=u'Eloy Adonis Colell',
    author_email='eloy.colell@gmail.com',
    packages=['amphipathic'],
    url='https://github.com/ecolell/amphipathic',
    license='MIT',
    description=('This is a library to evaluate an aminoacid sequence and '
                 'determine an amphipathic index for each alpha helix or '
                 'beta sheet.'),
    long_description=get_long_description(),
    zip_safe=True,
    install_requires=requirements,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
