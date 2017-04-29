# mputil -- Utility functions for
# Python's multiprocessing standard library module
#
# Author: Sebastian Raschka <mail@sebastianraschka.com>
# License: MIT
# Code Repository: https://github.com/rasbt/mputil

from .map import lazy_map
from .map import lazy_imap

__all__ = [lazy_map, lazy_imap]

__version__ = '0.1.0'
__author__ = "Sebastian Raschka <mail@sebastianraschka.com>"
