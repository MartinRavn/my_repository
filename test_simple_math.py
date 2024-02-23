"""
A collection tests for simple math operations
"""
#import pytest
import simple_math

def test_simple_add():
    assert simple_math.simple_add(1,2) == 3

def test_simple_sub():
    assert simple_math.simple_sub(3,2) == 1

def test_simple_mult():
    assert simple_math.simple_mult(8,9) == 72

def test_simple_div():
    assert simple_math.simple_div(72,9) == 8

def test_poly_first():
    assert simple_math.poly_first(100,50,0.1) == 60

def test_poly_second():
    assert simple_math.poly_second(2,3,2,1) == 11
