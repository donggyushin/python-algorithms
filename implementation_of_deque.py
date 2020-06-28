"""
Deque을 직접 구현해보기 전에 Deque의 기본적인 속성들과 메서드들을 살펴보자. 

Deque()는 비어있는 deque 객체를 생성한다. 파라미터는 받지 않고, 빈 deque객체를 반환한다. 
addFront(item)는 새로운 아이템을 deque의 front에 추가한다. 전달인자로 item을 받고 아무것도 반환하지 않는다. 
addRear(item)는 새로운 아이템을 deque의 rear 추가한다. 전달인자로 item을 받고 아무것도 반환하지 않는다. 
removeFront()는 deque의 front에서 item 하나를 제거하면서 해당 item을 반환한다. 이후에 deque은 변화한다. 
removeRear()는 deque의 rear에서 item 하나를 제거하면서 해당 item을 반환한다. 이후에 deque은 변화한다. 
isEmpty()는 deque이 비어있는지 확인한다. 전달인자는 받지 않고 boolean 값을 반환한다. 
size()는 deque이 몇개의 item들을 가지고 있는지를 integer 형으로 반환한다. 

"""


class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.size())
print(d.removeFront() + ' ' + d.removeRear())
print(d.size())
print(d.isEmpty())
