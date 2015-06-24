#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for py2cytoscape

To install, run:

python setup.py install
"""

from setuptools import setup, find_packages

setup(
    name='py2cytoscape',
    version='0.4.2',
    description='Tools to use Cytoscape and Cytoscape.js from Python',
    long_description='Collection of tools for using Cytoscape and '
                     'cytoscape.js from Python.  From v0.4.0, '
                     'it includes wrapper for Cytoscape\'s '
                     'cyREST App.',
    author='Keiichiro Ono',
    author_email='kono@ucsd.edu',
    url='https://github.com/idekerlab/py2cytoscape',
    license='MIT License',
    install_requires=[
        'pandas',
        'networkx',
        'requests',
        'python-igraph',
        'pyparsing',
        'scipy'
    ],
    keywords=['data visualization', 'visualization', 'cytoscape',
              'bioinformatics', 'graph', 'network'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    test_suite='tests',
    packages=find_packages(),
    include_package_data=True,
)
