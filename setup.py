#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Installation script for CFD book package '''

from setuptools import setup

# Get install requirements from requirements.txt file
with open('build_requirements.txt', 'rt') as fobj:
    install_requires = [line.strip() for line in fobj
                        if line.strip() and line[0] not in '#-']


setup(name='cfdcode',
      version=0.1,
      packages=['cfdcode'],
      license='BSD license',
      install_requires = install_requires,
      )
