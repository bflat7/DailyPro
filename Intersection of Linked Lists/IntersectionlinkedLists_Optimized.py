def intersection(a, b):
    if a is None or b is None:
        return None
    
    pointerA = a
    pointerB = b
    lastA = None
    lastB = None

    while True:
        if pointerA is pointerB:
            return pointerA
        
        if pointerA.next is None:
            lastA = pointerA
            pointerA = b
        else:
            pointerA = pointerA.next
        
        if pointerB.next is None:
            lastB = pointerB
            pointerB = a
        else:
            pointerB = pointerB.next
        
        if lastA is not None and lastB is not None and lastA is not lastB:
            return None


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val),
            c = c.next

# a = Node(1)
# a.next = Node(2)
# a.next.next = Node(3)
# a.next.next.next = Node(4)

# b = Node(6)
# b.next = a.next.next

# c = intersection(a, b)
# c.prettyPrint()