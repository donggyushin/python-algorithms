"""
n이라는 숫자를 받고, coin values들을 담고 있는 리스트를 받는다. 
해당 n을 구현하기 위한 가장 적은 코인들의 집합을 찾는 문제

예를 들어서 n = 10, coins = [1, 5, 10] 이라면 다음과 같은 4가지 방법으로 10 을 구현할 수 있다. 
1+1+1+1+1+1+1+1+1+1
5+1+1+1+1+1
5+5
10

마지막의 경우는 코인을 하나만 써서 해결했기 때문에 해당
케이스에는 마지막 경우가 정답

"""

from nose.tools import assert_equal
from typing import List


class TestCase(object):

    def test(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(45, coins), 3)
        assert_equal(solution(23, coins), 5)
        assert_equal(solution(74, coins), 8)
        print('PASSED ALL TESTS')

    def test2(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(45, coins, known_results), 3)
        assert_equal(solution(23, coins, known_results), 5)
        assert_equal(solution(74, coins, known_results), 8)
        print('PASSED ALL TESTS')


def rec_coin(target: int, coins: List[int]) -> int:
    # min_coins는 최종 결과값인데 우선은 target으로 셋팅해놈.
    min_coins = target

    # Base Case
    # 만약에 target이 coins 안에 속한다면 정답은 1 이므로 이렇게하고 끝
    if target in coins:
        return 1
    else:

        # For every coin value that is <= my target
        for i in [c for c in coins if c <= target]:
            # ADD A COIN COUNT + RECURSIVE
            # 코인의 갯수를 가져오는 recursive case
            # target 값에서 coin 만큼을 빼고, coin의 갯수를 1 추가해주면서 다시
            # target에서 빠져나간 coin 값만큼을 target 값으로 다시 주면서
            # 재귀함수를 재 호출
            num_coins = 1 + rec_coin(target - i, coins)
            # num_coins 가 min_coins(처음에 결과값으로 반환해주려고
            # 해준 초기값) 보다 작으면 계속해서 min_coins를 최신화
            if num_coins < min_coins:

                min_coins = num_coins

    # min_coins가 최신화가 끝나면 min_coins를 반환.

    return min_coins


target = 100
coins = [1, 5, 10, 25]
known_results = [0]*(target + 1)


def rec_coin_dynam(target: int, coins: List[int], known_results) -> int:
    # Default output to target
    min_coins = target
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:

        # For every coin value that is greater than target
        for i in [c for c in coins if c <= target]:

            num_coins = 1 + rec_coin_dynam(target - i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins

                # Reset that known results
                known_results[target] = min_coins

        return min_coins


t = TestCase()
t.test(rec_coin)
t.test2(rec_coin_dynam)
