from typing import List

"""
연속된 가장 큰 합

예를 들어서 다음과 같은 배열이 있다고 가정을 해보자. 
[1,2,-1,3,4,10,10,-10,-1]

여기서 숫자들을 연속해서 더했을때에 가장 높은 크기의 숫자를 구하는 문제이다. 
위에서는 배열의 0번째 인덱스부터 6번째 인덱스까지 더한
29 가 연속된 수의 합 중에서 가장 큰 값이다. 
"""

"""
첫번째 솔루션. 이 알고리즘 문제의 해결방법의 키는
current_sum과 max_sum 두개의 변수를 가지고 계속해서 current_sum 과 max_sum 을 업데이트 시켜주는 방법이다. 
current_sum 은 현재 배열을 순회하면서 값을 더해나갈때 큰 값을 저장하는 변수이고
max_sum은 지금까지의 current_sum 중에서의 가장 높은 값을 저장하는 변수이다. 

마지막에 max_sum을 리턴하면 문제 해결
"""


def largest_continuous_sum(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0

    max_sum = current_sum = 0

    for num in arr:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum


print(largest_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
