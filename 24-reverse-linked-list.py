#!/bin/python
"""
Write a function for reversing a linked list ↴ . Do it in-place ↴ .

Your function will have one input: the head of the list.

Your function should return the new head of the list.
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        print self.value



# given starting node.. iterate till the end
# we only need to change the pointers.. not the values
# destructive in place solution
last = None
linked_list = []
if not linked_list:
    return None # bail on empty linked list

node = linked_list[0] # gets the head

while node.next:
    copy = LinkedListNode(node.value) # create copy of node..
    copy.next = node.next             # might not be needed...

    node.next = last

    # go to next
    last = node
    node = copy.next

# return last good node head
return node
