"""
Fibonnaci Sequence

피보나치 수열 문제를 3개의 다른 방식으로 풀어봅시다!

Recursively
Dynamically (Using Memoization to store result)
Iteratively


"""

from nose.tools import assert_equal


def fib_rec(n: int):

    # Base Case
    if n == 0 or n == 1:
        return n
    # Recursive Case
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


n = 100
cache = [None] * (n + 1)


def fib_dyn(n: int):

    # Base Casee
    if n == 0 or n == 1:
        return n

    # Check Cache

    if cache[n] != None:

        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


def fib_iter(n: int):

    a = 0
    b = 1

    for _ in range(n):

        a, b = b, a + b
    return a


class TestCase(object):

    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)
        print('PASSED ALL TESTS')


t = TestCase()
t.test(fib_rec)
t.test(fib_dyn)
t.test(fib_iter)

"""
실질적인 코딩은 별로 어렵지 않다는 것을 느끼셨을겁니다. 
문제 해결을 하는데에 있어서 가장 어려운 부분은 바로
생각하는 부분이에요. 
그리고 그것이 바로 recursion 문제들이 가지고 있는 
특징이기도 해요. 
문제에 대해서 생각하는게 실제로 코딩하는 것보다
훨씬 더 어려워요 실은. 
그러니까 이 문제를 한번 풀어본걸로 끝내시지 마시고,
다시 한 번 문제를 되짚어보고, 내가 문제에 대해서
제대로 이해했나 다시 한 번 생각해보시길 추천드릴게요. 

그리고 여유가 되시는 분들은 한번 timeout library등을 이용
하셔서, 어떤 함수의 실행속도가 가장 빠른지도 한 번 제보시면 
재밌을 것 같아요. 
"""
