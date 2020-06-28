"""
2개의 스택을 이용하여서 Queue를 구현해보세요. 스택으로는 Python의 list를 사옹하시면 됩니다. 

Solution
이 문제를 해결하기 위한 key는 스택은 데이터의 삽입과 추출의 순서가 역순이라는 것을 이해한다는 점입니다. 
결과적으로 두개의 맞붙여진 스택은, 서로 데이터의 삽입과 추출의 순서가 서로 역방향이라는 점을 활용한다면
데이터의 삽입과 추출의 순서를 일치시키는 새로운 컬렉션 즉, queue를 하나 만들어낼 수 있습니다. 

그래서 우리는 두개의 스택을 각각 in-stack,out-stack 으로 구분지어서 사용할 것입니다. in-stack은 
새로운 element가 enqueue 되어질때 담아주는 stack이고, dequeue연산은 out-stack으로부터 요소들을
빼오게 합니다. 만약에 out-stack이 빈다면 우리는 in-stack의 모든 element들을 pop으로 빼내어서 
out-stack 에 넣어줍니다. 
"""


class Queue2Stacks(object):

    def __init__(self):

        self.instack = []
        self.outstack = []

    def enqueue(self, item):

        self.instack.append(item)

    def dequeue(self):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


q2s = Queue2Stacks()
q2s.enqueue(1)
q2s.enqueue(2)
q2s.enqueue(3)
print(q2s.dequeue())
print(q2s.dequeue())
print(q2s.dequeue())
