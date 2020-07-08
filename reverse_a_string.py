from nose.tools import assert_equal


"""
Reverse a string
이 인터뷰 문제는 recursion을 이용하여서 string을 reverse 시키는 문제입니다.
이 곳에서의 base case가 뭔지 잘 한 번 고민해보세요. 
slice(e.g. string[::-1]) 혹은 iteration을 사용하지 말고 꼭
recursion을 이용해서 풀어보세요

reverse('hello world') -> 'dlrow olleh'
"""


class TestReverse(object):

    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASE!')


def reverse(s: str) -> str:

    # Base Case
    if len(s) == 1:
        return s
    # Recursion
    return reverse(s[1:]) + s[0]


test = TestReverse()

test.test_rev(reverse)
