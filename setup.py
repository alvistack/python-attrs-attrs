# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='attrs',
    version='23.2.0',
    description='Classes Without Boilerplate',
    author_email='Hynek Schlawack <hs@ox.cx>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Typing :: Typed',
    ],
    install_requires=[
        'importlib-metadata; python_version < "3.8"',
    ],
    extras_require={
        'cov': [
            'attrs[tests]',
            'coverage[toml]>=5.3',
        ],
        'dev': [
            'attrs[tests]',
            'pre-commit',
        ],
        'docs': [
            'furo',
            'myst-parser',
            'sphinx',
            'sphinx-notfound-page',
            'sphinxcontrib-towncrier',
            'towncrier',
            'zope-interface',
        ],
        'tests': [
            'attrs[tests-no-zope]',
            'zope-interface',
        ],
        'tests-mypy': [
            'mypy>=1.6; platform_python_implementation == "CPython" and python_version >= "3.8"',
            'pytest-mypy-plugins; platform_python_implementation == "CPython" and python_version >= "3.8"',
        ],
        'tests-no-zope': [
            'attrs[tests-mypy]',
            'cloudpickle; platform_python_implementation == "CPython"',
            'hypothesis',
            'pympler',
            'pytest-xdist[psutil]',
            'pytest>=4.3.0',
        ],
    },
    packages=[
        'attr',
        'attrs',
    ],
    package_dir={'': 'src'},
)
