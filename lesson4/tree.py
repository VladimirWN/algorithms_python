from color import *
import random as rd


class Node:
    def __init__(self, value=None, left=None, right=None, color=Color.RED):
        self.value = value
        self.left = left
        self.right = right
        self.color = color

    def __str__(self):
        return f"value= {self.value}, color= {self.color.name}"


class Tree:
    def __init__(self, root: Node = None):
        self.root = root

    def __contains__(self, value):
        if self.root == None:
            return False
        node = self.root
        while node != None:
            if node.value == value:
                return True
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return False

    def add(self, value):
        if self.root:
            result = self.add_node(self.root, value)
            self.root = self.rebalance(self.root)
            if self.root.color == Color.RED:
                self.root.color = Color.BLACK
            return result
        else:
            self.root = Node(value, color=Color.BLACK)
            return True

    def add_node(self, node: Node, value):
        if node.value == value:
            return False
        else:
            if node.value > value:
                if node.left:
                    result = self.add_node(node.left, value)
                    node.left = self.rebalance(node.left)
                    return result
                else:
                    node.left = Node(value)
                    return True
            else:
                if node.right:
                    result = self.add_node(node.right, value)
                    node.right = self.rebalance(node.right)
                    return result
                else:
                    node.right = Node(value)
                    return True

    def rebalance(self, node: Node):
        result = node
        need_rebalance = True
        while need_rebalance:
            need_rebalance = False
            if result.right and result.right.color == Color.RED \
                    and (result.left == None or result.left.color == Color.BLACK):
                need_rebalance = True
                result = self.right_turn(result)
            if result.left and result.left.color == Color.RED \
                    and result.left.left and result.left.left.color == Color.RED:
                need_rebalance = True
                result = self.left_turn(result)
            if result.left and result.left.color == Color.RED and result.right and result.right.color == Color.RED:
                need_rebalance = True
                self.swap_color(result)
        return result

    def left_turn(self, node: Node):
        child_left = node.left
        child_between = node.right
        child_left.right = node
        node.left = child_between
        child_left.color = node.color
        node.color = Color.RED
        return child_left

    def right_turn(self, node: Node):
        child_right = node.right
        child_between = child_right.left
        child_right.left = node
        node.right = child_between
        child_right.color = node.color
        node.color = Color.RED
        return child_right

    def swap_color(self, node: Node):
        node.color = Color.RED
        node.left.color, node.right.color = Color.BLACK, Color.BLACK

    def print_tree(self, node: Node = None):
        if node == None:
            node = self.root
        if node.left:
            self.print_tree(node.left)
        print(node)
        if node.right:
            self.print_tree(node.right)


new_tree = Tree()
for i in range(10):
    num = rd.randint(0, 10)
    print("insert {}".format(num))
    print(new_tree.add(num))
    print("root", new_tree.root)
    new_tree.print_tree()
    print()
