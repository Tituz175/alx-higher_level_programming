#!/usr/bin/python3
"""This is a module defines a node of a singly linked list"""


class Node:
    """This is a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This function returns the data of the node"""
        return self.__data

    @property
    def next_node(self):
        """This function returns the next node of the list"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """This function sets the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """This function sets the next node of the list"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        printsll = ""
        location = self.__head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node

        return printsll[:-1]

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head
            if temp.data >= new_node.data:
                new_node.next_node = temp
                self.__head = new_node
            else:
                while (temp.next_node is not None and
                       temp.next_node.data < new_node.data):
                    temp = temp.next_node
                new_node.next_node = temp.next_node
                temp.next_node = new_node
