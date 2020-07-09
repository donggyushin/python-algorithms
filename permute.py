"""
Problem Statement

문자열을 받고, 해당 문자열로 조합 가능한 모든 순열을 반환하는 함수를 
작성하시오. 
For example, given s='abc' 라는 문자열을 받으면
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

만약에 중복되는 문자가 있다면, 각각의 문자들을
개별적인 문자로 인식하시오. 예를들어서
'xxx'는 6개의 'xxx'를 가진 리스트를
반환합니다. 
"""
from typing import List
from nose.tools import assert_equal

"""
Solutions

1. 처음으로 받은 문자열들을 반복한다
2. 처음으로 받은 이니셜의 각 문자들마다 나머지 남은 문자들의 모든 가능한 순열을 붙인다. 
permute란 함수는 받은 문자열들로 부터 가능한 모든 순열을 반환
하는 함수이기 때문에
예) 'abc' -> a + permute(bc) 이런식으로 쭉
가다보면 'abc' 가 가질 수 있는 모든 순열 조합을 얻을 수 있다. 
3. 2번 단계에서 리스트를 얻으면, 처음으로 받아온 문자열로부터 
나온 문자에 리스튿들의 모든 요소들을 합친다. 
그로부터 나온 리스트를 우리의 최종 output의 리스트에 더해준다. 
그래서 만약에 우리가 b에 있다면, 우리는 ['ac', 'ca']라는 리스트를 얻게 
될 것이고, 이를 b에 더하면 ['bac', 'bca'] 가 될것이다. 
4. 최종 리스트인 output을 반환한다. 
"""


class TestCase(object):

    def test(self, solution):

        assert_equal(sorted(solution('abc')), sorted(
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(
            ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print('ALL TEST CASES PASSED')


def permute(s):

    out = []

    # Base Case
    if len(s) == 1:
        out = [s]
    else:

        # for every letter in string
        for i, let in enumerate(s):

            # for every permutation resulting from step 2 and 3

            for perm in permute(s[:i] + s[i + 1:]):

                out += [let+perm]

    return out


t = TestCase()
t.test(permute)
