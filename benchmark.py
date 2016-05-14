"""Benchmark your regex by measuring the time it takes to execute."""
from time import clock as now


def test(func, *args, **kwargs):
    """Measure the time taken to execute a function."""
    start = now()
    func(*args, **kwargs)
    print "The function {} took {} sec.".format(func.__name__, now() - start)
