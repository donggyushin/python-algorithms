from typing import List

"""
Problem1

n을 입력받으면 0부터 n까지 숫자의 합을 반환하는 함수를 작성하시오. 
For example, if n = 4, return 4+3+2+1+0=, which is 10 
"""


def rec_sum(n: int) -> int:

    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)


print(rec_sum(4))


"""
Problem2
int형 숫자를 하나 받으면 각 숫자의 자릿수들을 모두 더한 값을 반환하는 함수를 작성하시오. 

For example:if n = 4321, return 4+3+2+1 
"""


def sum_func(n: int) -> int:

    if n == 0:
        return 0
    else:
        return n % 10 + sum_func(int(n / 10))


print(sum_func(1234))


"""
Problem3 

string이랑 단어들로 이루어진 리스트를 인자로 받고, 전달받은 string 값이 두번째로 전달받은 
리스트안에 들어있는 단어들에 의해서 완전하게 
split 될 수 있는지 확인하는 함수를 작성하시오. 

For example
word_split('themanran', ['the', 'man', 'ran', 'two']) -> ['the', 'man', 'ran']
word_split('themanran', ['1', '2', 'the', 'ran', 'women']) -> ['the']
word_split('themanran', ['clown', 'man', 'ran']) -> [] 
"""


def word_split(phrase: str, list_of_words: List[str], output=None) -> str:

    print(phrase)

    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)

    return output


print(word_split('themanran', ['clown', 'ran', 'man', '2']))
