from RomanNumeralsToDecimal import (Solution)
import unittest
import pytest

def test_NoneReturnsNone():
    assert Solution().romanToInt(None) is None

def test_OnlyAdditiveDifferentReturnsCorrectSum():
    assert Solution().romanToInt('MDCLXVI') == 1666

def test_OnlyAdditiveSameReturnsCorrectSum():
    assert Solution().romanToInt('MM') == 2000
    assert Solution().romanToInt('DD') == 1000
    assert Solution().romanToInt('CC') == 200
    assert Solution().romanToInt('LL') == 100
    assert Solution().romanToInt('XX') == 20
    assert Solution().romanToInt('VV') == 10
    assert Solution().romanToInt('II') == 2

def test_AdditiveWithSubtractiveReturnsCorrectSum():
    assert Solution().romanToInt('IV') == 4
    assert Solution().romanToInt('IX') == 9
    assert Solution().romanToInt('XL') == 40
    assert Solution().romanToInt('XC') == 90
    assert Solution().romanToInt('CD') == 400
    assert Solution().romanToInt('CM') == 900

def test_providedExample():
    assert Solution().romanToInt('MCMX') == 1910