# https://programmers.co.kr/learn/courses/30/lessons/17687

"""
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.15ms, 10.3MB)
테스트 6 〉	통과 (0.29ms, 10.3MB)
테스트 7 〉	통과 (0.17ms, 10.3MB)
테스트 8 〉	통과 (0.19ms, 10.3MB)
테스트 9 〉	통과 (0.20ms, 10.3MB)
테스트 10 〉	통과 (0.19ms, 10.3MB)
테스트 11 〉	통과 (0.39ms, 10.2MB)
테스트 12 〉	통과 (0.28ms, 10.2MB)
테스트 13 〉	통과 (0.20ms, 10.3MB)
테스트 14 〉	통과 (72.17ms, 10.4MB)
테스트 15 〉	통과 (44.84ms, 10.3MB)
테스트 16 〉	통과 (72.19ms, 10.4MB)
테스트 17 〉	통과 (2.55ms, 10.2MB)
테스트 18 〉	통과 (1.87ms, 10.4MB)
테스트 19 〉	통과 (0.50ms, 10.3MB)
테스트 20 〉	통과 (2.03ms, 10.4MB)
테스트 21 〉	통과 (9.08ms, 10.3MB)
테스트 22 〉	통과 (4.94ms, 10.2MB)
테스트 23 〉	통과 (12.78ms, 10.3MB)
테스트 24 〉	통과 (17.44ms, 10.3MB)
테스트 25 〉	통과 (15.60ms, 10.3MB)
테스트 26 〉	통과 (5.28ms, 10.3MB)
"""


def notation_10_n(x, n):
    expression = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    res = ''
    while x > 0:
        a, b = divmod(x, n)
        x = a

        if 10 <= b <= 15:
            res += expression[b]
        else:
            res += str(b)
    return res[::-1]


def solution(n, t, m, p):
    # "참가 인원 수 * 게임 턴 수" 길이를 갖는 답안을 만든다.
    target = m * t

    # 1부터 x까지 반복문 돌면서, 게임에서 요구하는 답안읆 만든다
    ans_everybody = '0'
    for x in range(1, 100001):  # 참가 인원 수 * 게임 턴 수 = 100000인데, 이보다 많은 숫자가 불리지는 않을 것이므로..
        ans_everybody += notation_10_n(x, n)
        if len(ans_everybody) >= target:
            break

    # # p부터 m의 간격으로 나의 답안을 찾는다.
    ans = ''
    for i in range(p, target + 1, m):
        ans += ans_everybody[i-1]
    return ans


if __name__ == '__main__':
    # "0111"
    n = 2  # 진법 (게임 규칙)
    t = 4  # 게임 턴 수 (내가 외쳐야 하는 숫자의 개수)
    m = 2  # 참가 인원
    p = 1  # 나의 순서

    # "02468ACE11111111"
    # n = 16
    # t = 16
    # m = 2
    # p = 1

    # "13579BDF01234567
    # n = 16
    # t = 16
    # m = 2
    # p = 2
    print(solution(n, t, m, p))