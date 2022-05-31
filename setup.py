#!/usr/bin/env python

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='reshact',
    py_modules=['reshact'],
    version='0.1.0',
    description='reshact is a command-line tool used to redact secrets in shell history',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/vesche/reshact',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    install_requires=[
        'click',
        'detect-secrets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)
