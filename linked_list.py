class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    def __repr__(self):
        return repr(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return str(nodes)

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        node = Node(value=value, next=self.head)
        if self.head:
            self.head.prev = node
        self.head = node

    def append(self, value):
        """Добавить элемент в конец списка"""
        if not self.head:
            self.prepend(value)
            return
        node = Node(value=value)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node

    def remove(self, value):
        """Удалить элемент"""
        current_node = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            if self.head:
                self.head.prev = None
            return
        while current_node and current_node.value != value:
            current_node = current_node.next
        if current_node is None:
            return
        if current_node.next:
            current_node.next.prev = current_node.prev
        if current_node.prev:
            current_node.prev.next = current_node.next

    def reverse(self):
        """Развернуть список"""
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = current_node.prev
            current_node.prev = next_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def _print(self):
        """Показать список"""
        print(self.__repr__())

link_list = DoublyLinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(5)
link_list.append(6)
link_list.append(8)
link_list._print()
link_list.reverse()
link_list._print()


