from MoveZeroesToEnd import (Solution)
import unittest
import pytest

def test_noneReturnsNone():
    assert Solution().moveZeros(None) == None

def test_swapZeroToEnd():
    nums = [0, 0, 12]
    Solution().moveZeros(nums)
    assert nums == [12, 0, 0]

def test_dontMoveEndZeroes():
    nums = [12, 0, 0]
    Solution().moveZeros(nums)
    assert nums == [12, 0, 0]

def test_moveAllZerosToEnd():
    nums = [0, 12, 3, 0, 9, 8]
    Solution().moveZeros(nums)
    assert nums == [12, 3, 9, 8, 0, 0]

def test_example():
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    Solution().moveZeros(nums)
    assert nums == [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]