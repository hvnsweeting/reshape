# -*- coding: utf-8 -*-

"""Top-level package for reshape."""

__author__ = """Viet Hung Nguyen"""
__email__ = 'hvn@familug.org'
__version__ = '0.1.0'


import itertools


def reshape(iterable, cols=3, rows=-1):
    '''Divide `iterable` to `cols` columns.

    '''

    # TODO determine cols when given rows
    N = len(iterable)
    each_col = N // cols
    remain = N % cols
    if remain != 0:
        each_col = each_col + 1

    chunks = [iterable[pos:pos+each_col] for pos in range(0, N, each_col)]
    # TODO support py2
    return [row for row in itertools.zip_longest(*chunks)]


def column(iterable, cols):
    return reshape(iterable, cols, rows=-1)
