from IntersectionlinkedLists_Optimized import (intersection, Node)
import unittest
import pytest

def test_emptyFirstParam_returnsNone():
    a =  Node(3)
    assert intersection(None, a) == None

def test_emptySecondParam_returnsNone():
    a = Node(3)
    assert intersection(a, None) == None

def test_noIntersection_returnsNone():
    a = Node(3)
    a.next = Node(4)
    a.next.next = Node(10)
    b = Node(1)
    b.next = Node(2)

    assert intersection(a, b) == None

def test_secondIntersectsFirst_returnsIntersection():
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    b = Node(6)
    b.next = a.next.next

    c = intersection(a, b)
    assert c is not None
    assert c.val == 3
    assert c.next.val == 4

def test_firstIntersectsSecond_returnsIntersection():
    b = Node(1)
    b.next = Node(2)
    b.next.next = Node(3)
    b.next.next.next = Node(4)
    a = Node(6)
    a.next = b.next.next

    c = intersection(a, b)
    assert c is not None
    assert c.val == 3
    assert c.next.val == 4