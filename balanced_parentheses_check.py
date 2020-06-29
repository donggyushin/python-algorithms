"""
parentheses
열어주는 parenthese와 닫아주는 parenthese로만 이루어진 문자열을 받는다. 그리고 해당 문자열이
balanced 되었는지 확인하는 알고리즘. 
우리는 총 3가지 종류의 parenthese를 전달 받을 수 있다. round brackets, square brackets,
square brackets. 위의 세가지 외에 다른 문자는 전달받지 않는다고 가정한다. 모든 parentheses는
열어주는 parenthese와 닫아주는 parenthese를 가지고 있어야 하며, 열어주고 닫아주는 위치가 
프로그래밍을 할때처럼 순서가 맞아야한다. 
예를들어서 ([])는 balanced parenthese가 맞고, {(}) 는 balanced parenthese가 아니다. 
"""

"""
Solution Key

해당 문제는 아주 자주 나오는 알고리즘 인터뷰 문제입니다. 그리고 이 문제의 핵심은 stack에 관해서 제대로
이해하고 있는지에 대한 문제이기도 합니다. 

그럼 balanced parenthese 를 해결하기 위한 logic 을 먼저 살펴보도록 하겠습니다. 

첫째로, 우리는 주어진 문자열을 왼쪽에서부터 오른쪽으로 한번 스캔할 것입니다. 그리고 우리는 열어주는 
parenthese를 볼때마다 스택에 넣어줄겁니다. 왜냐하면 우리는 가장 마지막에 나오는 열어주는 
parenthese가 가장 첫번째로 나오는 닫아주는 parenthese가 되어지길 원하기 때문입니다. 
(Stack의 First in last out 원칙)

그리고 나서, 우리가 닫아주는 parenthesis를 보게되면 우리는 stack으로부터 가장 마지막으로 나온
열려있는 parenthesis가 방금 처음으로 나온 닫아주는 parenthesis와 매치가 되는지 stack의 pop 
함수를 이용해서 확인 할 것입니다. 만약에 서로 매치가 된다면 계속해서 다음 단계로 넘어가고 그렇지
않다면 False를 반환해줍니다. 또한 stack이 비어있다면 False를 반환해주어야 합니다. stack이 비어
있다면 open된 parenthesis가 다 떨어져있다는 뜻이기 때문이죠. 그러면 닫히는 parenthesis와
매칭될 게 없으니끼 당연히 False겠죠? 그리고 닫혀진 parenthesis와 열리진 parenthesis를 모두
매칭시켜주었다면 stack이 비었는지 확인해주어야 합니다. stack이 비지 않았다면 False겠죠? 
열어주는 parenthesis의 갯수가 더 많다는 뜻이니까요. 
"""


def balance_check(s: str) -> bool:

    if len(s) % 2 != 0:
        return False

    opening = set('([{')

    matches = set([('(', ')'), ('{', '}'), ('[', ']')])

    # 파이썬의 list는 stack과 똑같이 사용할 수 있으므로 굳이 stack을 만들어서 문제를 푸실 필요 없습니다.
    stack = []

    for paren in s:

        if paren in opening:
            stack.append(paren)

        else:

            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


print(balance_check('[]('))
