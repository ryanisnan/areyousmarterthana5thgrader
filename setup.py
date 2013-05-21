#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='django-areyousmarterthana5thgrader',
    version='0.1.0',
    description='A very simple captcha form element for django',
    author='Ryan West',
    author_email='ryanisnan@gmail.com.com',
    url='http://github.com/ryanisnan/areyousmarterthana5thgrader/',
    long_description=open('README.md', 'r').read(),
    zip_safe=False
)