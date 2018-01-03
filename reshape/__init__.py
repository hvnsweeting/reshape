# -*- coding: utf-8 -*-

"""Top-level package for reshape."""

__author__ = """Viet Hung Nguyen"""
__email__ = 'hvn@familug.org'
__version__ = '0.3.0'


try:
    # Py2
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest


def chunk(iterable, chunksize):
    '''Divides `iterable` into chunks of chunksize.'''
    N = len(iterable)
    return [iterable[pos:pos+chunksize] for pos in range(0, N, chunksize)]


def reshape(iterable, cols=3, rows=-1):
    '''Divide `iterable` to `cols` columns.
    '''

    # TODO determine cols when given rows
    N = len(iterable)
    each_col = N // cols
    remain = N % cols
    if remain != 0:
        each_col = each_col + 1

    chunks = chunk(iterable, each_col)
    return list(zip_longest(*chunks))


def column(iterable, cols):
    '''#TODO UNIX column command like
    '''
    return reshape(iterable, cols, rows=-1)


def print_cols(iterable, cols=3, format_each="{}", col_sep=" ", **kwargs):
    format_all = col_sep.join([format_each] * cols)
    for line in column(iterable, cols):
        print(format_all.format(*line))


if __name__ == "__main__":
    print_cols(range(20), 3)
