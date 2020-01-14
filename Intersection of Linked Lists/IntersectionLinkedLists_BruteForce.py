def intersection(a, b):
    if a is None or b is None:
        return None
    return outterIterate(a, b)

def outterIterate(a, b):
    result = innerIterate(a, b)
    if a.next is None:
        return None
    elif result is None:
        return outterIterate(a.next, b)
    else:
        return result

def innerIterate(a, b):
    if a.val == b.val:
        return a
    elif b.next is not None:
        return innerIterate(a, b.next)
    else:
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

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()