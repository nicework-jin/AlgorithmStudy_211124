"""
https://programmers.co.kr/learn/courses/30/lessons/42746

테스트 1 〉	통과 (43.24ms, 23.3MB)
테스트 2 〉	통과 (22.12ms, 17.1MB)
테스트 3 〉	통과 (52.79ms, 27.4MB)
테스트 4 〉	통과 (0.98ms, 10.4MB)
테스트 5 〉	통과 (37.71ms, 21.8MB)
테스트 6 〉	통과 (31.60ms, 20.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
"""


def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(reverse=True, key=lambda x: x*4)
    ans = ''.join(numbers_str)

    if ans[0] == '0' and len(ans) > 1:
        return '0'
    else:
        return ans


if __name__ == "__main__":
    # 6210
    numbers = [6, 10, 2]

    # 9534330
    # numbers = [3, 30, 34, 5, 9]


    # 0
    numbers = [0, 0]
    print(solution(numbers))
