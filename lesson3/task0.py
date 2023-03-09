class User_list:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def __str__(self):
        lst = ""
        current = self.head
        while current:
            lst += str(current.value) + ", "
            current = current.next_node
        return f"{lst[:-2]}"

    def find(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node

    def add_first(self, value):
        current_node = Node(value)
        current_node.next_node = self.head
        self.head.previous_node = current_node
        self.head = current_node

    def delete_first(self):
        self.head = self.head.next_node
        self.head.previous_node = None

    def add_last(self, value):
        current_node = Node(value)
        self.tail.next_node = current_node
        current_node.previous_node = self.tail
        self.tail = current_node

    def delete_last(self):
        current_node = self.head
        while current_node:
            if not current_node.next_node.next_node:
                self.tail = current_node
                self.tail.next_node = None
            current_node = current_node.next_node

    def sort(self):
        current = self.head
        while current:
            temp = current
            while temp:
                if current.value > temp.value:
                    current.value, temp.value = temp.value, current.value
                else:
                    temp = temp.next_node
            current = current.next_node

# ДЗ: Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next_node
        return size

    def reverse(self):
        n = self.size()
        left = self.head
        right = self.tail
        for i in range(n // 2):
            left.value, right.value = right.value, left.value
            left, right = left.next_node, right.previous_node


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None

    def __str__(self) -> str:
        return f"{self.value}"


some_list = User_list(1)
some_list.add_first(2)
some_list.add_first(3)
some_list.add_first(4)
some_list.add_first(5)
print(some_list)

some_list.delete_first()
print(some_list)

some_list.add_last(6)
some_list.add_last(7)
some_list.add_last(8)
print(some_list)

some_list.delete_last()
print(some_list)

some_list.reverse()
print(some_list)

some_list.sort()
print(some_list)
