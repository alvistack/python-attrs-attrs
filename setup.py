# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='attrs',
    version='23.1.0',
    description='Classes Without Boilerplate',
    author_email='Hynek Schlawack <hs@ox.cx>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
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
            'attrs[docs,tests]',
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
        'tests-no-zope': [
            'cloudpickle; platform_python_implementation == "CPython"',
            'hypothesis',
            'mypy>=1.1.1; platform_python_implementation == "CPython"',
            'pympler',
            'pytest-mypy-plugins; platform_python_implementation == "CPython" and python_version < "3.11"',
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
