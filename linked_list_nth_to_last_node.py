"""
Problem statement 

링크드 리스트의 헤더를 받고, integer형 숫자 n을 받는다. 
그리고 마지막 노드로부터 n번째 node를 반환하는 함수를
작성하여라 
"""

"""
Solution

하나의 링크드 리스트를 가지고 있다고 생각해라. 그리고 n만큼의 node들이 담겨있는 블록을 있다고
생각해라. 
이 블록이 해당 리스트를 순회하는 것이다. 
이 블록은 left pointer와 right pointer를 가지고 있다. 
이 블록의 left pointer는 이 블락의 시작 노드이고, 
이 블록의 right pointer는 이 블록의 마지막 노드이다. 
이 블록의 right pointer가 링크드 리스트의
tail에 닿는 그 순간 해당 블록의 left-pointer 가
해당 링크드 리스트의 마지막 노드로부터 n번째 노드가 된다. 


"""


class Node(object):

    def __init__(self, value):

        self.value = value
        self.next: Node = None


def nth_to_last_node(n: int, head: Node) -> Node:

    left_pointer = head
    right_pointer = head

    for _ in range(n - 1):

        """
        만약에 전달받은 인자가 리스트의 길이보다 길 경우에
        얘기치 못한 에러가 발생할 수 있겠죠.
        이런 얘기치 못한 상황을 대비해서 미리 예외처리를
        해두는 것은 아주 좋은 습관입니다. 
        """
        if not right_pointer.next:

            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.next

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(nth_to_last_node(2, a).value)
