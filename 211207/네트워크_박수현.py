"""
https://programmers.co.kr/learn/courses/30/lessons/43162

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.13ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.10ms, 10.3MB)
테스트 9 〉	통과 (0.11ms, 10.3MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.46ms, 10.4MB)
테스트 12 〉	통과 (0.37ms, 10.3MB)
테스트 13 〉	통과 (0.18ms, 10.3MB)

조건
- 연결된 네트워크의 개수를 리턴
1. computer[i][i] = 1 (자신)

알고리즘
1. 방문하지 않은 정점 방문
2. 해당 정점과 이웃하고 방문하지 않은 경우 방문한다.
3. 1-2를 마치면 한 네트워크임으로 정답+1
"""
from collections import deque


def dfs(i, computers, visited):
    visited[i] = True
    for j in range(len(computers)):
        # 2
        if computers[i][j] == 1 and not visited[j]:
            dfs(j, computers, visited)


def bfs(i, computers, visited):
    q = deque([i])
    while q:
        i = q.popleft()
        visited[i] = True
        for j in range(len(computers)):
            # 2
            if computers[i][j] == 1 and not visited[j]:
                q.append(j)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    # 1
    for i in range(len(computers)):
        if not visited[i]:
            dfs(i, computers, visited)
            # 3
            answer += 1
    return answer
