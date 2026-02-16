# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='attrs',
    version='25.4.0',
    description='Classes Without Boilerplate',
    author_email='Hynek Schlawack <hs@ox.cx>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Typing :: Typed',
    ],
    packages=[
        'attr',
        'attrs',
    ],
    package_dir={'': 'src'},
)
