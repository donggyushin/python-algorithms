"""
Array Pair Sum

숫자 배열이 주어졌을때, 특정 값을 만족시키는 유니크한 쌍들을 모두 찾아내는 문제

[1,3,2,2], 4 가 주어졌을때
(1,3), (2,2) 이런 식으로 두 숫자의 값이 4를 만족시키는 모든 쌍들을 찾아내야한다. 

"""


def pair_sum(arr: [int], k: int) -> int:

    # 우선 배열의 길이가 2보다 작으면 한쌍도 나올수없으니깐 0을 리턴한다

    if len(arr) < 2:
        return 0

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        # 해당 num당 구해야하는 target
        target = k - num
        # 해당 target을 본적이 없다면 이 target에해당하는 숫자 num 을 seen에 넣어줘요. 그렇다면 이 seen에 들어가는 값은 나중에 언젠가는 제대로된 짝을 만나면
        # target값이 되어질 겁니다.
        # 나중에 target값이 여기 seen에 속하게 된다면, 저희는 그 target과 해당 target에 해당하는 숫자 num 으로
        # 튜플 데이터 하나를 만들어서 output set data에 넣어줍니다.
        # 이 output 데이터 스트럭쳐는 set 데이터이기 때문에, 중복된 값이 들어오게 된다면 해당 쌍을 축적하지 않을거에요. 저희는 특정 값을 만족시키는
        # 유니크한 쌍들을 찾아내고 있기 때문에, set 데이터 스트럭쳐를 이용한다면 해당 문제는 아주 간단하게 이렇게 해결할수가 있어요.
        # 그래서 이 문제같은 경우는 올바른 데이터 스트럭쳐를 이용할 줄 아느냐, 를 물어보기 위한 알고리즘 테스트라고도 볼 수 있어요.
        # 이렇게 중복없이 유니크한 값들만 추려내려 한다면, set 데이터 스트럭쳐를 이용하는건 어떨지 한번 고민해보는게 좋습니다.
        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))
            print((min(num, target), max(num, target)))

    return len(output)


print(pair_sum([1, 3, 2, 2], 4))
