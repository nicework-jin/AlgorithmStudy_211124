"""
https://programmers.co.kr/learn/courses/30/lessons/42861

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)

조건
- 최소 비용으로 모든 섬을 통행하도록 만들 때 필요한 최소 비용을 구하라

크루스칼 알고리즘(최소 신장 트리) 활용 문제
- 탐욕법을 이용하여 가장 적은 비용으로 모든 노드를 연결
1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 최소 비용의 간선을 선택하고 현재의 간선이 사이클을 발생시키는지 확인
2-1. 발생하지 않는 경우 최소 신장 트리에 포함시킴
2-2. 발생하는 경우 포함시키지 않음
3. 방문하지 않은 모든 간선에 대하여 2번 과정을 반복
"""


def solution(n, costs):
    answer = 0
    # 1
    costs.sort(key=lambda x: x[2])
    routes = set([costs[0][0]])
    while len(routes) != n:
        # 2
        for i, cost in enumerate(costs):
            # 2-2 둘 다 집합 안에 있다면 사이클이 존재하기 때문에 재탐색
            if cost[0] in routes and cost[1] in routes:
                continue
            # 2-1 최소 신장트리에 간선을 포함시킴
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                # 해당 값을 다시 사용하지 않기 위함
                costs[i] = [-1, -1, -1]
                break
    return answer


