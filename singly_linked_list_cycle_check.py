"""
Singly linked list cycle check 

이 문제는 해당 리스트가 순환하는 리스트인지, 아닌지를 알아보는 문제입니다. 

하나의 싱글 링크드 리스트가 주어질때, 해당 리스트의 첫번째 노드를 받고 해당
리스트가 순환하는 링크드 리스트인지, 아닌지에 따라서 True or False 
를 반환하는 함수를 작성하세요. 

순환하는 리스트란 노드의 다음 포인터가 자신보다 앞에 있는 노드를 가리켜서 
노드의 다음 포인터를 계속해서 따라가다 보면
순회를 멈추지 않고 계속해서 돌게되는 리스트를 말합니다. 
"""


"""
Solution

이 문제를 해결하기 위해선 해당 리스트를 순회하는 두개의 marker가 필요합니다. 
우리는 첫번째 노드부터 시작하는 두개의 marker를 가지고, 둘의 이동속도를 다르게
맞춰줄 겁니다. 
marker1은 한턴당 한칸씩 움직이게 되고, 
marker2는 한턴당 두칸씩 움직이게 됩니다. 
marker2가 움직이다가 혹여라도 먼저 리스트의 끝에
도달하게 된다면 해당 리스트는 순환하는
리스트가 아닙니다. 하지만 순환하는 리스트라면 
marker1과 marker2의 이동속도는 서로 다르기 때문에
언젠가 한 번쯤은 마주치게 되어있습니다. 
따라서 무한 반복문을 돌다가 marker1과 marker2가 동일하게
된다면 해당 리스트는 순환하는 링크드 리스트가 되어집니다. 

"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next: Node = None


def cycle_check(node: Node) -> bool:

    runner1 = node
    runner2 = node

    while runner2 != None and runner2.next != None:

        runner1 = runner1.next
        runner2 = runner2.next.next

        if runner1 == runner2:
            return True

    return False


# cycle list
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

# non cycle list

x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z


print(cycle_check(a))
print(cycle_check(x))
