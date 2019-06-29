# -*- coding: UTF-8 -*-
from setuptools import (find_packages, setup)

long_description = '''Financial Indicator Tool

Install : pip install indicator

Upgrade : pip install --upgrade indicator

'''

setup(
    name='indicator',
    version='1.0.3',
    keywords='Financial Indicator Tool',
    description='Solving Quantitative Indicators of Funds, Stocks and Foreign Exchange Tool',
    long_description=long_description,
    author='Tab',
    author_email='ns_v@sina.com',
    url='https://github.com/haibeicode/indicator',
    install_requires=['pandas', 'numpy'],
    packages=find_packages(),
    license='Apache 2.0',
)
