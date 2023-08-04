from collections import deque
import queue as q
from multiprocessing import Queue

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node()
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "empty"
        else:
            return self.linkedList.head