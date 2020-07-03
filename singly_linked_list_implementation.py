
"""
이번 시간에는 링크드 리스트를 구현해줄거에요. 
"""

# 우선 node라는 클래스를 하나 만들어줄겁니다.


class Node(object):

    def __init__(self, value):
        # node는 value값을 가지고있고, 자신의 다음 노드를 가리키는 포인터도 가지고 있기 때문에,
        # 전달 인자로 value를 받아서, 본인의 value에 저장시켜주시고,
        # 다음 노드를 가리키는 nextNode 라는 reference를 만들어주세요.
        # 타입은 본인과 똑같은 node이고, 우선은 None값을 줍니다.
        self.value = value
        self.nextNode: Node = None


# 그리고 3개의 노드를 만들어줄게요.
a = Node(1)
b = Node(2)
c = Node(3)

# 그리고 순서는 a,b,c가 되도록 nextNode의 값을 다음과 같이 만들어주도록 하겠습니다.
a.nextNode = b
b.nextNode = c


# a의 value값, 1이 제대로 찍히고,
print(a.value)
# a의 다음 node인 b의 value값 2도 제대로 찍히고,
print(a.nextNode.value)
# b의 다음 node인 c의 value값도 제대로 찍히고 있죠?
print(b.nextNode.value)


"""
링크드 리스트의 장점과 단점에 대해서 설명해보라는 인터뷰 질문은 자주 나오는 질문이기 때문에, 
한번 정리하고 넘어갈게요.


Pros
장점으로는 

링크드 리스트는 어떤 위치에서건 삽입과 제거하는데 동일한 시간이 소요된다. 일반적인 배열은 해당 작업을 실행하기 위해선
O(n) 만큼의 복잡도를 가진다. 

링크드 리스트는 미리 리스트의 사이즈를 정해주지 않아도 무한정으로 사이즈를 확장시킬 수 있다. 


Cons
그리고 단점으로는 

링크드 리스트에 있는 요소에 접근하기 위해서, 해당 요소까지 접근하려면 O(k) 만큼의 복잡도를 갖는다. 하지만 배열에서는
해당 작업을 수행하는데 일정한 시간만을 소요한다. 





수고하셨습니다! 싱글 링크드 리스트를 구현해보았습니다. 다음 시간에는 Doubly linked list 에 대해서 배워보도록 할게요. 
"""
