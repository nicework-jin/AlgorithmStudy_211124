"""
https://programmers.co.kr/learn/courses/30/lessons/42883

테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (0.20ms, 10.4MB)
테스트 6 〉	통과 (3.02ms, 10.4MB)
테스트 7 〉	통과 (8.97ms, 10.4MB)
테스트 8 〉	통과 (18.69ms, 11MB)
테스트 9 〉	통과 (43.85ms, 16.1MB)
테스트 10 〉	통과 (105.43ms, 14.7MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)

반례
# 53
number = 5321
k = 2
"""

from collections import deque


def solution(number, k):
    number = deque(number)

    stack = []
    while number:
        n = number.popleft()

        while stack and stack[-1] < n:
            if k == 0:
                break
            stack.pop()
            k -= 1
        stack.append(n)

    ans = ''.join(stack)
    if k != 0:
        return ans[:len(number)-k]
    return ans


if __name__ == '__main__':
    # 94
    number = "1924"
    k = 2

    # 3234
    number = "1231234"
    k = 3

    # "775841"
    number = "4177252841"
    k = 4

    # 5321
    number = "5321"
    k = 2

    print(solution(number, k))

