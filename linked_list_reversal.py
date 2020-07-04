"""
Problem

링크드 리스트를 역전시키는 함수를 작성하시오 
"""

"""
Solution

해당 문제를 해결하기 위해서 하나의 리스트를 더 만들어주는 방식으로 하면
복잡하지 않게 해결할 수 있다. 
하지만 그런식으로 위의 문제를 해결하게 된다면 복잡도는 O(n) 이 된다. 
링크드 리스트를 역전시키는데는 O(1) 만큼의 복잡도만 있어도 충분하다. 
그 방법은 각각 노드의 포인터를 자기 이후의 노드가 아닌, 
자기 이전의 노드를 가리키게만 하면 된다. 
"""


class Node(object):

    def __init__(self, value):

        self.value = value
        self.next: Node = None


def see_all_nodes(node: Node):
    currentNode = node
    while currentNode:
        print(currentNode.value)
        currentNode = currentNode.next


def reverse_linked_list(node: Node):

    prev_node = None
    current_node = node
    next_node = None

    while current_node:

        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

see_all_nodes(a)
new_header = reverse_linked_list(a)
see_all_nodes(new_header)
