# https://programmers.co.kr/learn/courses/30/lessons/60057
"""

테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.36ms, 10.2MB)
테스트 3 〉	통과 (0.18ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.75ms, 10.3MB)
테스트 8 〉	통과 (0.49ms, 10.2MB)
테스트 9 〉	통과 (0.56ms, 10.3MB)
테스트 10 〉	통과 (2.25ms, 10.3MB)
테스트 11 〉	통과 (0.15ms, 10.3MB)
테스트 12 〉	통과 (0.09ms, 10.3MB)
테스트 13 〉	통과 (0.10ms, 10.2MB)
테스트 14 〉	통과 (0.60ms, 10.2MB)
테스트 15 〉	통과 (0.10ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (1.86ms, 10.3MB)
테스트 18 〉	통과 (1.72ms, 10.2MB)
테스트 19 〉	통과 (1.07ms, 10.3MB)
테스트 20 〉	통과 (2.43ms, 10.3MB)
테스트 21 〉	통과 (2.47ms, 10.3MB)
테스트 22 〉	통과 (2.85ms, 10.3MB)
테스트 23 〉	통과 (2.90ms, 10.2MB)
테스트 24 〉	통과 (2.34ms, 10.2MB)
테스트 25 〉	통과 (4.56ms, 10.3MB)
테스트 26 〉	통과 (2.73ms, 10.3MB)
테스트 27 〉	통과 (2.57ms, 10.3MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)
"""


def solution(s):
    k = len(s) // 2
    mn = 1001

    while k > 0:
        s_copy = s

        cnt = 1
        ff = ''
        while s_copy != '':
            tmp = s_copy[:k]
            s_copy = s_copy[k:]

            if ff[-k:] == tmp:
                cnt += 1
            else:
                if cnt >= 2:
                    ff += str(cnt)
                    cnt = 1
                ff += tmp
        else:
            if cnt >= 2:
                ff += str(cnt)

        mn = min(mn, len(ff))
        k -= 1

    if mn == 1001:
        return 1
    else:
        return mn


if __name__ == '__main__':
    #  1개는 할 필요가 없음. 어차피 문자열 길이와 같음

    #  절반 길이 ~ 2 까지 줄여가며 수행! 이때 수행하는 길이를 n이라고 정의
    #  시작점은 0 ~ n-1
    #  시간 복잡도는 길이가 2일 때가 최악! 총 길이 1000일때 501번
    #  501 + 333 + ... . .. 이므로 그다지 크지 않음.

    # 7
    s = "aabbaccc"

    # 9
    # s = "ababcdcdababcdcd"

    # 8
    # s = "abcabcdede"

    # 14
    s = "abcabcabcabcdededededede"

    # 17
    # s = "xababcdcdababcdcd"

    # 1
    # s = 'a'
    print(solution(s))