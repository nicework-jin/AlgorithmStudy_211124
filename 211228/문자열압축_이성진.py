"""
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.65ms, 10.3MB)
테스트 3 〉	통과 (0.22ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.48ms, 10.2MB)
테스트 8 〉	통과 (0.47ms, 10.4MB)
테스트 9 〉	통과 (0.74ms, 10.3MB)
테스트 10 〉	통과 (2.81ms, 10.3MB)
테스트 11 〉	통과 (0.10ms, 10.3MB)
테스트 12 〉	통과 (0.11ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.92ms, 10.2MB)
테스트 15 〉	통과 (0.12ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (1.23ms, 10.3MB)
테스트 18 〉	통과 (1.25ms, 10.2MB)
테스트 19 〉	통과 (1.22ms, 10.3MB)
테스트 20 〉	통과 (2.77ms, 10.2MB)
테스트 21 〉	통과 (2.96ms, 10.3MB)
테스트 22 〉	통과 (2.78ms, 10.3MB)
테스트 23 〉	통과 (2.70ms, 10.3MB)
테스트 24 〉	통과 (2.69ms, 10.3MB)
테스트 25 〉	통과 (2.77ms, 10.2MB)
테스트 26 〉	통과 (2.75ms, 10.3MB)
테스트 27 〉	통과 (2.82ms, 10.2MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
"""


def solution(s):
    if len(s) < 3:
        return 1

    mn = 99999
    for interval in range(1, len(s)//2+1):
        res = ''

        # interval 간격으로 쪼개기
        tmp = []
        for i in range(0, len(s), interval):
            tmp.append(s[i:i+interval])

        # 앞뒤로 붙어있는 문자열 선형적으로 탐색
        idx = 0
        k = len(tmp)
        while idx <= k-1:
            cnt = 1
            while idx < k-1 and tmp[idx] == tmp[idx+1]:
                cnt += 1
                idx += 1
            if cnt > 1:
                res += str(cnt) + tmp[idx]
            else:
                res += tmp[idx]
            idx += 1
        mn = min(mn, len(res))
    return mn


if __name__ == '__main__':
    s = "abcabcdede"
    s = "aabbaccc"
    s = "ababcdcdababcdcd"
    s = "abcabcabcabcdededededede"
    s = "xababcdcdababcdcd"
    s = 'a'
    print(solution(s))
