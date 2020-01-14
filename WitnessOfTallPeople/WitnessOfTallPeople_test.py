from WitnessOfTallPeople import (witnesses)
import unittest
import pytest

def test_noneReturnsNone():
    assert witnesses(None) is None

def test_shortBlockedByTall():
    heights = [1, 2]
    assert witnesses(heights) == 1

def test_tallNotBlockedByShort():
    heights = [2, 1]
    assert witnesses(heights) == 2

def test_sameBlocks():
    heights = [2, 2]
    assert witnesses(heights) == 1

def test_example():
    heights = [3, 6, 3, 4, 1]
    assert witnesses(heights) == 3