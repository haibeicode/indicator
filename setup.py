# -*- coding: UTF-8 -*-
import os
 
import setuptools
 
setuptools.setup(
    name='indicator',
    version='2019.06.26',
    keywords='quant indicator',
    description='quant indicator tool',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='haibei',
    author_email='ns_v@sina.com',
 
    url='https://github.com/haibeicode/indicator', 
    packages=setuptools.find_packages(),
    license='APACHE'
)
