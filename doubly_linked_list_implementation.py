"""
이번 시간에는 저번시간에 배운 더블 링크드 리스트를 직접 구현해서
추상적이었던 개념을 조금 더 구체화해서 익혀보도록 할께요. 
"""


class DoublyLinkedListNode(object):

    def __init__(self, value):
        self.value = value
        """
        더블 링크드 리스트는 싱글 링크드 리스트와는 다르게 자기 이후의 노드를 가리키는 next pointer도 있지만
        자신의 이전 노드를 가리키는 prev pointer도 있습니다. 
        """
        self.next: DoublyLinkedListNode = None
        self.prev: DoublyLinkedListNode = None


"""
그리고 더블 링크드 리스트의 업데이트가 제대로 이루어졌는지 확인을 위한 
함수도 하나 만들어줄게요. 
해당 노드를 시작점으로 하여서 리스트를 끝까지 
순회하는 함수입니다. 
"""


def seeAllNodes(node: DoublyLinkedListNode):

    currentNode = node

    while True:
        print(currentNode.value)
        currentNode = currentNode.next
        if not currentNode:
            break


"""
이제 노드 3개를 만들어주고 a,b,c 순서대로 리스트에 정렬시켜줄께요
"""
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next = b
b.prev = a
b.next = c
c.prev = b

"""
제대로 정렬이 됬는지 확인해봐야겠죠
"""
seeAllNodes(a)

"""
그리고 이번에는 b를 지워보도록 할께요
"""

print("deleting node b...")

a.next = c
c.prev = a


seeAllNodes(a)

"""
이렇게 이번에 아주 간단하고 직관적으로 더블 링크드 리스트에 대해서 배워보았어요
다음 시간에는 링크드 리스트에 관해서 더 이야기해보고
링크드 리스트와 관련된 면접 문제에 대해서도 알아보도록 해요

"""
