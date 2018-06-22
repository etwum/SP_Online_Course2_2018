"""
test_generator.py

tests the solution to the generator lab

can be run with py.test or nosetests
"""
import pytest
import generator as gen


def test_int_sum():

    g = gen.int_sum()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_doubler():

    g = gen.doubler()

    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 4
    assert next(g) == 8
    assert next(g) == 16
    assert next(g) == 32

    for i in range(10):
        j = next(g)

    assert j == 2**15