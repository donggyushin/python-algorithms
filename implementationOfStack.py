"""
Stack() - 새로운 stack 인스턴스를 하나 만든다. 필요한 파라미터는 없고 빈 스택객체를 하나 생성한다. 
push(item) - 새로운 item을 stack 객체의 꼭대기에 집어넣는다. 파라미터로 item을 하나 받고 아무것도 리턴하지 않는다. 
pop() - 스택의 가장 꼭대기 아이템을 제거한다. 파라미터는 필요로 하지 않고 item 하나를 반환한다. 스택은 변경되어진다. 
peek() - 스택의 가장 꼭대기에 있는 아이템을 보여준다. 하지만 제거하지는 않는다. 스택은 변경되지 않는다. 
isEmpty() - 스택이 비어있는지 확인한다. boolean 값을 반환한다. 
size() - 스택안에 있는 아이템들의 갯수를 반환한다. 파라미터를 필요로 허지 않고 integer를 반환한다. 
"""


class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(1)
s.push('two')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
