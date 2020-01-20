from NthFibonacciNumber import (Solution)
import unittest
import pytest

def test_NoneReturnsNone():
    assert Solution().fibonacci(None) is None

def test_FibonacciSequence():
    assert Solution().fibonacci(0) == 0
    assert Solution().fibonacci(1) == 1
    assert Solution().fibonacci(2) == 1
    assert Solution().fibonacci(3) == 2
    assert Solution().fibonacci(4) == 3
    assert Solution().fibonacci(5) == 5
    assert Solution().fibonacci(6) == 8
    assert Solution().fibonacci(7) == 13
    assert Solution().fibonacci(9) == 34
    assert Solution().fibonacci(13) == 233
