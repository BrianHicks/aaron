#!/usr/bin/env python
from setuptools import setup, find_packages

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
        import multiprocessing
except ImportError:
        pass

setup(
    name = 'Aaron',
    version = '1.1.0',
    packages = find_packages(),

    # testing
    test_suite = 'nose.collector',
    tests_require = ['nose'],

    # metadata for PyPi and others
    author = 'Brian Hicks',
    author_email = 'brian@brianthicks.com',
    description = 'Nice function composition',
    license = 'TODO',
    url = 'https://github.com/BrianHicks/aaron',
    download_url = 'https://github.com/BrianHicks/aaron',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ]
)
