# mputil -- Utility functions for
# Python's multiprocessing standard library module
#
# Author: Sebastian Raschka <mail@sebastianraschka.com>
# License: MIT
# Code Repository: https://github.com/rasbt/mputil

from setuptools import setup, find_packages


def calculate_version():
    initpy = open('mputil/__init__.py').read().split('\n')
    version = list(filter(lambda x:
                          '__version__' in x, initpy))[0].split('\'')[1]
    return version


package_version = calculate_version()

setup(name='mputil',
      version=package_version,
      description="Utility functions for Python's multiprocessing module",
      author='Sebastian Raschka',
      author_email='mail@sebastianraschka.com',
      url='https://github.com/rasbt/mputil',
      license='MIT',
      zip_safe=True,
      packages=find_packages(),
      platforms='any',
      keywords=['multiprocessing'],
      classifiers=[
             'License :: OSI Approved :: MIT License',
             'Development Status :: 5 - Production/Stable',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: POSIX',
             'Operating System :: Unix',
             'Operating System :: MacOS',
             'Programming Language :: Python :: 3.5',
             'Topic :: Scientific/Engineering',
      ],
      long_description="""
mputil is a package that provides utility functions for
Python's multiprocessing standard library module


Contact
=============

If you have any questions or comments about mputil, please feel
free to contact me via
eMail: mail@sebastianraschka.com
or Twitter: https://twitter.com/rasbt

This project is hosted at https://github.com/rasbt/mputil

""")
