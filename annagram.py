# annagram이란?

"""
두개의 문자열이 각자 문자열을 구성하고 있는 문자의 출현 빈도수가 서로 일치할 경우 annagram이라고 한다. 
예를 들어서 Dog와 God, clint eastwood, old west action 등이 있다. 

그래서 이 말을 다르게 하면, 두개의 문자열이 한 번 정렬이 되고 난 이후에 서로 같은 모양을 띄게 된다면 두 문자열은 서로 annagram이 된다는 뜻이다.
"""
# 먼저 아주 쉬운 방법이 있다. sorted 라는 파이썬 내장 함수를 이용하는 방식읻다. 
def annagram1(s1:str,s2:str) -> bool:

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

# 면접에서 annagram에 대해서 물어볼 경우 이 두번째 방식으로 문제 해결하는 능력을 보여주는 것이
# 면접관들이 더욱 원하는 방식
# 각각의 문자들의 갯수를 비교해서 annagram을 판별해보자. 
def annagram2(s1:str, s2:str) -> bool:

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case check
    if len(s1) != len(s2):
        return False

    count = {} 

    for letter in s1:
        if count[letter]:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if count[letter]:
            count[letter] -= 1
        else:
            count[letter] = -1
    
    for k in count:
        if count[k] != 0:
            return False 
    
    return True


    