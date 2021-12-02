"""
https://programmers.co.kr/learn/courses/30/lessons/43165

테스트 1 〉	통과 (342.68ms, 10.3MB)
테스트 2 〉	통과 (334.27ms, 10.3MB)
테스트 3 〉	통과 (0.35ms, 10.2MB)
테스트 4 〉	통과 (1.33ms, 10.3MB)
테스트 5 〉	통과 (10.21ms, 10.2MB)
테스트 6 〉	통과 (0.69ms, 10.2MB)
테스트 7 〉	통과 (0.35ms, 10.2MB)
테스트 8 〉	통과 (2.72ms, 10.2MB)
"""


def solution(numbers, target):
    num = 0

    def DFS(L, x):
        nonlocal num
        if L == len(numbers):
            if x == target:
                num += 1
        else:
            DFS(L + 1, x - numbers[L])
            DFS(L + 1, x + numbers[L])
    DFS(0, 0)
    return num


if __name__ == '__main__':
    # 5
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))