import math
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if l1 is None and l2 is None:
        return None
    
    if l1 is None and l2 is not None:
      return l2
    elif l1 is not None and l2 is None:
      return l1

    firstNumber = secondNumber = 0
    multiplier = 1
    while l1:
        firstNumber += l1.val * multiplier
        multiplier *= 10
        l1 = l1.next
    multiplier = 1
    while l2:
        secondNumber += l2.val * multiplier
        multiplier *= 10
        l2 = l2.next
    total = firstNumber + secondNumber
    
    return self.deconstructNumber(total, 10)

  def deconstructNumber(self, val, multiplier):
    value = val % multiplier
    if value == 0:
      return None
    
    newVal = val - value
    thisListNode = ListNode((value / multiplier) * 10)
    thisListNode.next = self.deconstructNumber(newVal, multiplier * 10)
    return thisListNode



# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print(result.val)
#   result = result.next
# 7 0 8