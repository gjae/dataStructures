"""
Implementation of a Singly Linked List data structure in Python.
A linked list is a linear data structure where elements are stored in nodes,
and each node points to the next node in the sequence.
"""

class Node:
    """Node class represents a single element in the linked list."""
    def __init__(self, data = None):
        """
        Initialize a node with data and next pointer.
        
        Parameters:
        data (any, optional): The value to store in the node. Defaults to None.
        """
        self.data = data    # Stores the data/value of the node
        self.next = None    # Reference to the next node (initially None)


class SinglyLinkedList:
    """Singly Linked List class that manages the collection of nodes."""
    def __init__(self):
        """
        Initialize an empty linked list.
        The head attribute points to the first node in the list.
        """
        self.head = None    # Head pointer initialized to None (empty list)

    def add(self, content):
        """
        Add a new node at the beginning of the list (prepend operation).
        
        Parameters:
        content (any): The data/value to be added to the new node.
        """
        if self.head is None:
            # If list is empty, create first node
            self.head = Node(content)
        else:
            # Create new node and insert at beginning
            new = Node(content)
            new.next = self.head  # New node points to current head
            self.head = new      # Update head to point to new node

    def words(self):
        """
        Generator function that yields each element in the list.
        
        Yields:
        any: The data/value of each node in sequence.
        
        Usage:
        for item in list.words():
            print(item)
        """
        current = self.head       # Start at the head of the list
        while current:           # Traverse until end of list (None)
            content = current.data  # Get current node's data
            current = current.next  # Move to next node
            yield content          # Yield the data to caller


# Example usage of the linked list
l_list = SinglyLinkedList()  # Create new linked list instance

# Add elements to the list (they will be added in reverse order)
l_list.add("Eggs")  # Becomes third item when we print
l_list.add("Ham")   # Becomes second item
l_list.add("Rise")  # Becomes first item

# Iterate through and print all elements in the list
for c in l_list.words():
    print(c)  # Output will be: Rise, Ham, Eggs (LIFO order)