#!/bin/python

"""
You have a singly-linked list ↴ and want to check if it contains a cycle.
A singly-linked list is built with nodes, where each node has:

node.next—the next node in the list.
node.value—the data held in the node. For example, if our linked list stores people in line at the movies, node.value might be the person's name.

A cycle occurs when a node’s next points back to a previous node in the list. The linked list is no longer linear with a beginning and end—instead, it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.
"""
# assume that if we see a duplicate value.. its cyclical.
# we are dealing with unique objects
# this solutions takes N space... N time
def contains_cycle(head_node):
    """returns boolean if has cycle"""
    seen_nodes = []
    while head_node:
        if head_node.value in seen_nodes:
            return True
        else:
            seen_nodes.append(head_node.value)
            head_node = head_node.next

    return False

### SPOILER
### actual solution algorithm is to code up two windows
### at different speeds...
