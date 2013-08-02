#!/usr/bin/env python
import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload -r internal')
    sys.exit()

setup(
        name = "pyscribe",
        version = "0.10",
        description="python scribe client",
        long_description=open("README.md").read(),
        author="yancl",
        author_email="kmoving@gmail.com",
        url='https://github.com/yancl/pyscribe',
        classifiers=[
            'Programming Language :: Python',
        ],
        platforms='Linux',
        license='MIT License',
        zip_safe=False,
        dependency_links = [
            "http://pypi.zhw.com:9000/packages/pyfb303-0.1.tar.gz",
        ],
        install_requires=[
            'pyfb303'
        ],
        packages=['scribe']
)