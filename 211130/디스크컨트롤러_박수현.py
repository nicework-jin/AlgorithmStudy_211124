"""
https://programmers.co.kr/learn/courses/30/lessons/42627

정확성  테스트
테스트 1 〉	통과 (8.76ms, 10.4MB)
테스트 2 〉	통과 (6.64ms, 10.3MB)
테스트 3 〉	통과 (4.91ms, 10.2MB)
테스트 4 〉	통과 (4.60ms, 10.3MB)
테스트 5 〉	통과 (7.36ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (4.19ms, 10.3MB)
테스트 8 〉	통과 (3.00ms, 10.3MB)
테스트 9 〉	통과 (0.61ms, 10.3MB)
테스트 10 〉	통과 (8.87ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)

조건 
- 하드디스크는 한 번에 하나의 작업만 수행

입출력
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
"""
"""
알고리즘
1. 현 시점에서 처리 가능한 작업을 힙에 삽입
- 처리 가능한 작업: 작업 요청 시간이 이전 작업 시작 시간(start)보다 크고 현 시점(now)보다 작거나 같을 때 힙에 삽입
2. 소요시간 기준으로 최소힙 생성
3. 최소힙에서 pop한 후에(실행시간 가장 적은 요소가 나옴) 현 시간 변수들 갱신
4. 힙이 비었다면 현 시간 1 증가
"""




import heapq
def solution(jobs):
    answer, now, cnt = 0, 0, 0
    heap = []
    start = -1
    while cnt < len(jobs):
        for job in jobs:
            # 1
            if start < job[0] <= now:
                # 2
                heapq.heappush(heap, (job[1], job[0]))
        # 3
        if len(heap) > 0:
            heap_term, heap_start = heapq.heappop(heap)
            start = now
            now += heap_term
            answer += (now - heap_start)
            cnt += 1
        # 4
        else:
            now += 1
    return answer//len(jobs)
