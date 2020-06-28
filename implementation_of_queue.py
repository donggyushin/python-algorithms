"""
Queue Methods and Attributes

우리가 직접 Queue를 구현해보기 전에 Queue가 가진 속성들과 함수들을 알아봅시다

Queue() 는 빈 큐 객체를 하나 생성합니다. 파라미터는 필요로 하지 않고, 빈 큐 객체 하나를 반환합니다. 
enqueue(item)은 큐의 rear에 새로운 item 을 하나 추가합니다. 파라미터로 아이템을 받고 아무것도 반환하지 않습니다. 
dequeue()는 큐의 front에서 item을 하나 제거합니다. 파라미터를 필요로 하지 않고 item하나를 반환합니다. 큐가 변화합니다. 
isEmpty()는 큐가 비어있는지를 확인합니다. 파라미터를 필요로 하지 않고, boolean 값을 반환합니다. 
size()는 큐가 지니고 있는 아이템들의 갯수를 반환합니다. 파라미터를 받지 않고 integer형 값을 반환합니다.
"""


class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())
print(q.size())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.isEmpty())
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())
print(q.size())
