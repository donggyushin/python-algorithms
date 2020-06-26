"""
sentence reversal

"Hello World" 와 같은 문자열이 주어졌을때 
"World Hello" 이런식으로 단어는 바뀌지 않고 단어의 순서가 바뀌는 알고리즘
"""

from typing import List


def rev_word1(s: str) -> str:
    return " ".join(reversed(s.split()))


"""
Solution

단어들만 담는 리스트를 하나 만들어서, 
해당 리스트를 역순으로 출력해준다. 
"""


def rev_word(s: str) -> str:

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and s[i] not in spaces:

                i += 1

            word_end = i

            words.append(s[word_start:word_end])

        i += 1

    return " ".join(reversed(words))


def rev_words(words: List[str]) -> List[str]:
    # words 리스트를 역순으로 반환해주는 함수를 직접 작성해보세요
    return []


print(rev_word("Hello World"))
