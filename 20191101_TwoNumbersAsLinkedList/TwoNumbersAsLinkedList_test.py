from TwoNumbersAsLinkedList import (Solution, ListNode)
import unittest

class test_TwoNumbersAsLinkedList(unittest.TestCase):
    def test_NonePassedInReturnsNone(self):
        assert Solution().addTwoNumbers(None, None) is None

    def test_EitherNodeNoneReturnsNonEmptyNode(self):
        l1 = ListNode(1)
        l1.next = ListNode(8)
        l1.next.next = ListNode(3)
        result = Solution().addTwoNumbers(None, l1)
        result2 = Solution().addTwoNumbers(l1, None)
        assert result.val == result2.val == 1
        assert result.next.val == result2.next.val == 8
        assert result.next.next.val == result2.next.next.val == 3

    def test_AllSingleDigitsReturnsProperSum(self):
        l1 = ListNode(1)
        l1.next = ListNode(8)
        l1.next.next = ListNode(3)
        l2 = ListNode(6)
        l2.next = ListNode(1)
        l2.next.next = ListNode(2)
        result = Solution().addTwoNumbers(l1, l2)
        assert result.val == 7
        assert result.next.val == 9
        assert result.next.next.val == 5

    def test_SumMultiDigitReturnsProperSum(self):
        l1 = ListNode(4)
        l1.next = ListNode(8)
        l1.next.next = ListNode(4)
        l2 = ListNode(7)
        l2.next = ListNode(8)
        l2.next.next = ListNode(3)
        result = Solution().addTwoNumbers(l1, l2)
        assert result.val == 1
        assert result.next.val == 7
        assert result.next.next.val == 8

    def test_SumFourDigitFromThreeDigitsReturnsProperSum(self):
        l1 = ListNode(1)
        l1.next = ListNode(3)
        l1.next.next = ListNode(7)
        l2 = ListNode(2)
        l2.next = ListNode(4)
        l2.next.next = ListNode(7)
        result = Solution().addTwoNumbers(l1, l2)
        assert result.val == 3
        assert result.next.val == 7
        assert result.next.next.val == 4
        assert result.next.next.next.val == 1