class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = Node

    def add(self, content):
        if self.head is None:
            self.head = Node(content)
        else:
            new = Node(content)
            new.next = self.head
            self.head = new

    def words(self):
        current = self.head
        while current:
            content = current.data
            current = current.next
            yield content


l_list = SinglyLinkedList()
l_list.add("Eggs")
l_list.add("Ham")
l_list.add("Rise")

for c in l_list.words():
    print(c)