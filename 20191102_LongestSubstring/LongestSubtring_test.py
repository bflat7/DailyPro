from LongestSubstring import (Solution)
import unittest

class test_LongestSubstring(unittest.TestCase):
    def test_NoneReturnsNone(self):
        assert Solution().lengthOfLongestSubstring(None) is None
    
    def test_EmptyStringReturnsZero(self):
        assert Solution().lengthOfLongestSubstring('') == 0

    def test_SingleLetterReturnsOne(self):
        assert Solution().lengthOfLongestSubstring('a') == 1
    
    def test_DuplicateLetterReturnsOne(self):
        assert Solution().lengthOfLongestSubstring('aa') == 1
    
    def test_SubsequentDuplicatesReturnsTwo(self):
        assert Solution().lengthOfLongestSubstring('aabb') == 2
    
    def test_ExampleReturnsTen(self):
        assert Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx') == 10

