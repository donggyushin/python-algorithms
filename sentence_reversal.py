"""
sentence reversal

"Hello World" 와 같은 문자열이 주어졌을때 
"World Hello" 이런식으로 단어는 바뀌지 않고 단어의 순서가 바뀌는 알고리즘
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


print(rev_word("Hello World"))
