# mputil -- Utility functions for
# Python's multiprocessing standard library module
#
# Author: Sebastian Raschka <mail@sebastianraschka.com>
# License: MIT
# Code Repository: https://github.com/rasbt/mputil

import multiprocessing as mp
from itertools import islice


def lazy_map(data_processor, data_generator, n_cpus=1, stepsize=None):
    """A variant of multiprocessing.Pool.map that supports lazy evaluation

    As with the regular multiprocessing.Pool.map, the processes are spawned off
    asynchronously while the results are returned in order. In contrast to
    multiprocessing.Pool.map, the iterator (here: data_generator) is not
    consumed at once but evaluated lazily which is useful if the iterator
    (for example, a generator) contains objects with a large memory footprint.

    Parameters
    ==========
    data_processor : func
        A processing function that is applied to objects in `data_generator`

    data_generator : iterator or generator
        A python iterator or generator that yields objects to be fed into the
        `data_processor` function for processing.

    n_cpus=1 : int (default: 1)
        Number of processes to run in parallel.
        - If `n_cpus` > 0, the specified number of CPUs will be used.
        - If `n_cpus=0`, all available CPUs will be used.
        - If `n_cpus` < 0, all available CPUs - `n_cpus` will be used.

    stepsize : int or None (default: None)
        The number of items to fetch from the iterator to pass on to the
        workers at a time.
        If `stepsize=None` (default), the stepsize size will
        be set equal to `n_cpus`.

    Returns
    =========
    list : A Python list containing the results returned
        by the `data_processor` function when called on
        all elements in yielded by the `data_generator` in
        sorted order. Note that the last list may contain
        fewer items if the number of elements in `data_generator`
        is not evenly divisible by `stepsize`.
    """
    if not n_cpus:
        n_cpus = mp.cpu_count()
    elif n_cpus < 0:
        n_cpus = mp.cpu_count() - n_cpus

    if stepsize is None:
        stepsize = n_cpus

    results = []

    with mp.Pool(processes=n_cpus) as p:
        while True:
            r = p.map(data_processor, islice(data_generator, stepsize))
            if r:
                results.extend(r)
            else:
                break
    return results


def lazy_imap(data_processor, data_generator, n_cpus=1, stepsize=None):
    """A variant of multiprocessing.Pool.imap that supports lazy evaluation

    As with the regular multiprocessing.Pool.imap, the processes are spawned
    off asynchronously while the results are returned in order. In contrast to
    multiprocessing.Pool.imap, the iterator (here: data_generator) is not
    consumed at once but evaluated lazily which is useful if the iterator
    (for example, a generator) contains objects with a large memory footprint.

    Parameters
    ==========
    data_processor : func
        A processing function that is applied to objects in `data_generator`

    data_generator : iterator or generator
        A python iterator or generator that yields objects to be fed into the
        `data_processor` function for processing.

    n_cpus=1 : int (default: 1)
        Number of processes to run in parallel.
        - If `n_cpus` > 0, the specified number of CPUs will be used.
        - If `n_cpus=0`, all available CPUs will be used.
        - If `n_cpus` < 0, all available CPUs - `n_cpus` will be used.

    stepsize : int or None (default: None)
        The number of items to fetch from the iterator to pass on to the
        workers at a time.
        If `stepsize=None` (default), the stepsize size will
        be set equal to `n_cpus`.

    Returns
    =========
    list : A Python list containing the *n* results returned
        by the `data_processor` function when called on
        elements by the `data_generator` in
        sorted order; *n* is equal to the size of `stepsize`. If `stepsize`
        is None, *n* is equal to `n_cpus`.
    """
    if not n_cpus:
        n_cpus = mp.cpu_count()
    elif n_cpus < 0:
        n_cpus = mp.cpu_count() - n_cpus

    if stepsize is None:
        stepsize = n_cpus

    with mp.Pool(processes=n_cpus) as p:
        while True:
            r = p.map(data_processor, islice(data_generator, stepsize))
            if r:
                yield r
            else:
                break
