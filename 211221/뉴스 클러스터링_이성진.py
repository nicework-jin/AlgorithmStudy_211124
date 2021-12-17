# https://programmers.co.kr/learn/courses/30/lessons/17677

"""
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.83ms, 10.1MB)
테스트 5 〉	통과 (0.06ms, 10.1MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.11ms, 10.1MB)
테스트 8 〉	통과 (0.04ms, 10.1MB)
테스트 9 〉	통과 (0.10ms, 10.3MB)
테스트 10 〉	통과 (0.16ms, 10.1MB)
테스트 11 〉	통과 (0.25ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
테스트 13 〉	통과 (0.09ms, 10.1MB)
"""

from collections import Counter


def solution(str1, str2):
    a = []
    for i in range(1, len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            a.append(str1[i-1].upper() + str1[i].upper())

    b = []
    for i in range(1, len(str2)):
        if str2[i - 1].isalpha() and str2[i].isalpha():
            b.append(str2[i - 1].upper() + str2[i].upper())

    # 집합연산 가능한 형태(Counter)로 개수 세기
    a_cnt = Counter(a)
    b_cnt = Counter(b)

    # 교집합, 합집합
    intersection = a_cnt & b_cnt
    union = a_cnt | b_cnt

    if not union:
        return 1 * 65536
    else:
        return int((sum(intersection.values()) / sum(union.values())) * 65536)


if __name__ == '__main__':
    # 16384
    str1 = 'FRANCE'
    str2 = 'french'

    # 65536
    # str1 = 'handshake'
    # str2 = 'shake hands'

    # # 43690
    # str1 = 'aa1+aa2'
    # str2 = 'AAAA12'
    #
    # # 65536
    # str1 = 'E=M*C^2'
    # str2 = 'e=m*c^2'

