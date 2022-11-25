#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['numpy', 'python-lzf']

setup_requirements = []


setup(
    author="Daniel Maturana",
    author_email='dimatura@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    description="Read and write PCL .pcd files in python.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pypcd',
    name='pypcd',
    packages=find_packages(include=['pypcd']),
    setup_requires=setup_requirements,
    url='https://github.com/map4/pypcd',
    version='0.1.2',
    zip_safe=False,
)
