from LargestProductOf3 import (maximum_product_of_three)
import unittest
import pytest

def test_noneReturnsNone():
    assert maximum_product_of_three(None) == None

def test_listSizeOneReturnsSingleValue():
    assert maximum_product_of_three([10]) == 10

def test_listSizeTwoReturnsProduct():
    assert maximum_product_of_three([10, 2]) == 20

def test_allPositivesReturnsTop3Product():
    assert maximum_product_of_three([1, 2, 3, 4]) == 24

def test_allNegativesReturnsTop3Product():
    assert maximum_product_of_three([-1, -2, -3, -4]) == -6

def test_avoidSingleNegative():
    assert maximum_product_of_three([1, 2, 3, -4]) == 6

def test_combinedRuleset():
    assert maximum_product_of_three([1, -4, 3, -6, 7, 0]) == 168

def test_twoNegativesOverTwoPositives():
    assert maximum_product_of_three([-4, -4, 2, 1, 8]) == 128