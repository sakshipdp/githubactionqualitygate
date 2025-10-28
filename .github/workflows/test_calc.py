import pytest
import calc
# tests/test_calc.py
from calc import add

def test_add():
    assert add(2, 3) == 5

#from calc import add,sub,mul,div

#def test_add():
#compare actual output and expected output
  # assert add(2, 3) == 5

def test_sub():
   assert sub(3, 1) == 2

def test_mul():
   assert mul(4, 2) == 8

def test_div():
   assert div(4, 2) == 2
