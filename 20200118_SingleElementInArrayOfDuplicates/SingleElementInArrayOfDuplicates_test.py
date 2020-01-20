from SingleElementInArrayOfDuplicates import (Solution)
import unittest

class TestTest(unittest.TestCase):
    def test_NoneReturnsNone(self):
        assert Solution().findSingle(None) is None

    def test_AllDuplicatesReturnsNone(self):
        assert Solution().findSingle([1, 1, 3, 3, 5, 5]) is None

    def test_SingleElementReturnsElement(self):
        assert Solution().findSingle([1]) == 1

    def test_AllDuplicatesOneSingleReturnsSingle(self):
        assert Solution().findSingle([1, 5, 6, 8, 1, 6, 8]) == 5

    def test_ProvidedExample(self):
        assert Solution().findSingle([1, 1, 3, 4, 4, 5, 6, 5, 6]) == 3