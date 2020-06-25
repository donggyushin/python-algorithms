import collections
from typing import List

"""
Find the missing element 문제
두 배열이 주어졌다고 가정을 하자. 

[1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]

여기서 두번째 배열은 첫번째 배열중에서 하나의 요소가 없어진 배열이다. 
어떤 요소가 사라졌는지 찾아보는 문제
"""


# 첫번째 솔루션.
"""
첫번째 솔루션은 바로 두 배열을 정렬시킨 다음에
각각 요소들을 비교해서, 처음으로 요소의 값이 서로 일치하지 않는 경우가
제거된 요소값이 되어진다. 
"""


def finder(arr1: List[int], arr2: List[int]) -> int:
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


"""
두번째 솔루션은 딕셔너리를 이용한 방법이다. 
딕셔너리는 알고리즘 문제에서 많이 사용되어지는 자료형인데, 바로 키값과 밸류값으로 이루어진 자료형이다. 
어떤 특정 숫자를 키값으로 놓고 그 숫자의 갯수를 밸류값으로 넣어서
특정 숫자값의 밸류값이 서로 다른 특정 숫자를 찾아내는 방법이다. 
"""


def finder2(arr1: List[int], arr2: List[int]) -> int:

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


print(finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
