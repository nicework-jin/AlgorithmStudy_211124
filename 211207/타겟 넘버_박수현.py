"""
https://programmers.co.kr/learn/courses/30/lessons/43165

정확성  테스트
테스트 1 〉	통과 (541.17ms, 99.8MB)
테스트 2 〉	통과 (527.89ms, 99.7MB)
테스트 3 〉	통과 (0.47ms, 10.3MB)
테스트 4 〉	통과 (1.86ms, 10.6MB)
테스트 5 〉	통과 (16.76ms, 12.6MB)
테스트 6 〉	통과 (0.98ms, 10.3MB)
테스트 7 〉	통과 (0.45ms, 10.3MB)
테스트 8 〉	통과 (4.19ms, 10.7MB)

조건
- numbers에 담긴 숫자를 더하거나 빼서 target을 만드는 경우의 수 구하기
1. numbers는 음수가 아님

알고리즘
1. 큐에 (연산값, 계산 횟수)를 넣고 반복
2. 마지막 연산일 때 target과 같다면 정답 1증가

"""

from collections import deque


def dfs(numbers, target):
    answer = 0
    # 1
    q = deque([(0, 0)])
    while q:
        result, idx = q.popleft()
        # 2
        if len(numbers) == idx:
            if result == target:
                answer += 1
        else:
            q.append((result+numbers[idx], idx+1))
            q.append((result-numbers[idx], idx+1))
    return answer


def solution(numbers, target):
    return dfs(numbers, target)
