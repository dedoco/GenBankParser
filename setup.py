#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

from setuptools import setup, find_packages

setup(
    name='GenbankParser',
    version='0.1-alpha',
    description='Unofficial parser for ncbi GenBank data.',
    author='Jonas I. Liechti',
    packages=find_packages(),
    install_requires=['configparser', 'requests'],
    data_files=[
        ('gbparse', ['gbparse/config.cfg']),
        ],
    include_package_data=True,
    )
