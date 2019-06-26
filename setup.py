# -*- coding: UTF-8 -*-
import os
from setuptools import (find_packages, setup)


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='indicator',
    version=read('indicator/VERSION.txt'),
    keywords='Financial Indicator Tool',
    description='Solving Quantitative Indicators of Funds, Stocks and Foreign Exchange Tool',
    long_description=read('indicator/README.md'),
    author='Tab',
    author_email='ns_v@sina.com',
    url='https://github.com/haibeicode/indicator',
    install_requires=['pandas', 'numpy', 'math'],
    packages=find_packages(),
    license='Apache 2.0',
)
