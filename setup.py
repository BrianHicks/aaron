from setuptools import setup, find_packages

setup(
    name = 'Aaron',
    version = '0.0.0',
    packages = find_packages(),

    # testing
    test_suite = 'runtests.runtests',
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
    ],

    long_description = open('README.md').read(),
)