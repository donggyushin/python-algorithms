"""
ㅇㅣ번 시간에 배워볼 알고리즘은 string_compression 입니다. 
'AAAAPPPBBBC' 이라는 문자열을 입력 받았을 때
A4P3B3C1 이런식으로 문자를 압축시켜주는 알고리즘입니다. 
"""


def compress(s: str) -> str:
    # 우선 결과 문자열이 될 문자열 r을 선언해줍니다.
    r = ""
    # 전달받은 문자열의 길이를 체크해주고,
    l = len(s)
    # edge case를 처리해줍니다.
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    # 위의 edge case를 건너 뛰었다면 문자열은 1개 이상이므로, 두번째 인덱스의 문자열부터 코드를 짜줍니다.
    # 카운트는 1, 그리고 인덱스도 0이 아닌 1로 잡아줍니다.
    cnt = 1
    i = 1
    # 인덱스가 문자열의 길이를 넘지 않을때까지 while문을 돌려주고,
    while i < l:
        # 이전 인덱스의 문자열과 같다면 count를 1씩 늘려줍니다.
        if s[i] == s[i-1]:
            cnt += 1
        else:
            # 이전 인덱스의 문자열과 다르다면 이전 문자의 갯수가 count만큼 있다는 거니 결과 문자열인 r 을 다음과 같이 업데이트 해주고
            # count를 1로 초기화해줍니다.
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1
    # 마지막 문자는 위의 while문에서 else 구문을 들어가지 못하게 되므로
    # while문이 끝나고 나면은 결과물이 될 문자열인 r을 마지막으로 업데이트 시켜주고 반환해줍니다.
    r = r + s[i-1] + str(cnt)
    return r


print(compress('AAAAPPPBBBC'))
