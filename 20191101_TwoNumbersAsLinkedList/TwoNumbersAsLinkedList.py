import math
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if l1 is None or l2 is None:
        return None
    
    firstNumber = 0
    secondNumber = 0
    firstMultiplier = 1
    while l1:
        firstNumber += firstNumber * firstMultiplier
        firstMultiplier *= 10
    secondMultiplier = 1
    while l2:
        secondNumber += secondNumber * secondMultiplier
        secondMultiplier *= 10
    totalMultiplier = max(firstMultiplier, secondMultiplier)

    # while totalMultiplier > 0:
    total = firstNumber + secondNumber
    
    return ListNode(10)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8