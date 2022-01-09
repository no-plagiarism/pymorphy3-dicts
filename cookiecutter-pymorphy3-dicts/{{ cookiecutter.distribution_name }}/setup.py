#!/usr/bin/env python
from setuptools import setup

setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    url='https://github.com/no-plagiarism/pymorphy3-dicts',

    description='{{ cookiecutter.lang_full }} dictionaries for pymorphy3',
    long_description=open('README.rst').read(),

    license='GPLv3 License',
    packages=['{{ cookiecutter.package_name }}'],
    package_data={'{{ cookiecutter.package_name }}': ['data/*']},
    zip_safe=False,
    entry_points={'pymorphy3_dicts': "{{ cookiecutter.lang }} = {{ cookiecutter.package_name }}"},

    classifiers=[
        'Development Status :: {{ cookiecutter.dev_status }}',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
