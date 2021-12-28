# https://programmers.co.kr/learn/courses/30/lessons/72413

# 직접 코드 짜볼 것. 아래 주소로부터 얻은 코드임
# https://gist.github.com/Chocochip101/40ea387899905740a646cb921698347f#file-2021kakao_problem4-1-py


"""
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (0.11ms, 10.3MB)
테스트 6 〉	통과 (0.19ms, 10.3MB)
테스트 7 〉	통과 (0.29ms, 10.3MB)
테스트 8 〉	통과 (0.25ms, 10.3MB)
테스트 9 〉	통과 (0.29ms, 10.3MB)
테스트 10 〉	통과 (0.33ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (19.50ms, 10.5MB)
테스트 2 〉	통과 (84.29ms, 11.6MB)
테스트 3 〉	통과 (36.64ms, 11.3MB)
테스트 4 〉	통과 (37.07ms, 11.3MB)
테스트 5 〉	통과 (36.11ms, 11.4MB)
테스트 6 〉	통과 (37.29ms, 11.4MB)
테스트 7 〉	통과 (929.91ms, 16.5MB)
테스트 8 〉	통과 (853.98ms, 16.9MB)
테스트 9 〉	통과 (799.64ms, 16.9MB)
테스트 10 〉	통과 (799.22ms, 16.9MB)
테스트 11 〉	통과 (745.52ms, 16.8MB)
테스트 12 〉	통과 (486.23ms, 14.2MB)
테스트 13 〉	통과 (485.55ms, 14MB)
테스트 14 〉	통과 (484.04ms, 14.3MB)
테스트 15 〉	통과 (451.70ms, 14.2MB)
테스트 16 〉	통과 (28.70ms, 11.4MB)
테스트 17 〉	통과 (31.71ms, 11.4MB)
테스트 18 〉	통과 (31.63ms, 11.3MB)
테스트 19 〉	통과 (79.74ms, 11.7MB)
테스트 20 〉	통과 (126.77ms, 12MB)
테스트 21 〉	통과 (126.00ms, 12.2MB)
테스트 22 〉	통과 (447.04ms, 14.2MB)
테스트 23 〉	통과 (452.43ms, 14.3MB)
테스트 24 〉	통과 (484.71ms, 14.2MB)
테스트 25 〉	통과 (21.75ms, 11.3MB)
테스트 26 〉	통과 (18.68ms, 11.1MB)
테스트 27 〉	통과 (111.22ms, 10.7MB)
테스트 28 〉	통과 (112.39ms, 10.8MB)
테스트 29 〉	통과 (10.85ms, 10.4MB)
테스트 30 〉	통과 (11.21ms, 10.4MB)
"""

import heapq


def solution(n, s, a, b, fares):
    # 양방향 링크 생성 [idx: 노드번호, 값: z, 노드가 가르키는 방향: y 또는 x]
    link = [[] for _ in range(n+1)]
    for x, y, z in fares:
        link[x].append((z, y))
        link[y].append((z, x))

    # 다익스트라 알고리즘 구현
    def dijkstra(start):
        # 최소 비용을 담을 리스트 [idx: 노드번호]
        dist = [987654321] * (n + 1)

        # 시작 노드의 초기값 설정
        dist[start] = 0

        # 인자 값은 (누적 최소비용, 다음 목적지)
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue

            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist

    # 각 지점에서 출발했을 때 나타나는 비용 [s, a, b는 각각 1이상이므로 맨 앞에 빈 리스트 추가]
    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]

    # for arr in dp:
    #     print(arr)

    answer = 987654321
    for i in range(1, n+1):
        # i는 합승하차노드 ... link는 방향이 없으므로, 합승하차노드로부터 출발지 + 각각 도착지로 이동한 최소비용
        # i에서 a, b, s로 가는 최소 비용을 합했을 때 최소값 [s:출발지, a는 A의 도착지, b는 B의 도착지]
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer


if __name__ == '__main__':
    # 82
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

    print(solution(n, s, a, b, fares))