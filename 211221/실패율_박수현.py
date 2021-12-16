"""
https://programmers.co.kr/learn/courses/30/lessons/42889

정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (1.21ms, 10.6MB)
테스트 4 〉	통과 (6.30ms, 10.8MB)
테스트 5 〉	통과 (18.79ms, 14.9MB)
테스트 6 〉	통과 (0.12ms, 10.4MB)
테스트 7 〉	통과 (0.84ms, 10.2MB)
테스트 8 〉	통과 (6.39ms, 10.9MB)
테스트 9 〉	통과 (18.86ms, 15MB)
테스트 10 〉	통과 (6.52ms, 10.8MB)
테스트 11 〉	통과 (7.11ms, 10.8MB)
테스트 12 〉	통과 (10.52ms, 11.4MB)
테스트 13 〉	통과 (11.70ms, 11.3MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (4.48ms, 10.5MB)
테스트 16 〉	통과 (2.16ms, 10.3MB)
테스트 17 〉	통과 (4.27ms, 10.6MB)
테스트 18 〉	통과 (2.15ms, 10.4MB)
테스트 19 〉	통과 (0.45ms, 10.2MB)
테스트 20 〉	통과 (3.22ms, 10.3MB)
테스트 21 〉	통과 (6.41ms, 10.8MB)
테스트 22 〉	통과 (18.70ms, 18.4MB)
테스트 23 〉	통과 (14.60ms, 11.6MB)
테스트 24 〉	통과 (12.87ms, 11.7MB)
테스트 25 〉	통과 (0.01ms, 10.4MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)

조건
- N: 전체 스테이지 수, stages: 도전 중인 스테이지 번호 배열
- 실패율: 도달했으나 클리어 못한 플레이어 수 / 스테이지 도달 플레이어 수
- 실패율이 높은 스테이지부터 스테이지 번호가 담겨있는 배열 return

1. stages(도전 중인 스테이지 번호): 1이상 N+1 이하의 자연수
N+1 = 마지막 스테이지 클리어
2. 실패율이 같다면 작은 번호의 스테이지가 먼저
3. 중요: 도달한 유저가 없는 경우 실패율 = 0 (0으로 나눌 경우 런타임 에러 발생)

알고리즘
1. stopped = {"stage번호": 도달한 사람 수}
2. failure = {"n번째 stage 번호": n의 수 / (전체 - n 미만의 수)}
3. 실패율 내림차순 정렬, 같은 경우 작은 번호가 먼저
"""
from collections import defaultdict
def solution(N, stages):
    stopped = defaultdict(int)
    failure = defaultdict(list)
    total_people = len(stages)
    result = []
    
    for stage in stages:
        stopped[stage] += 1
    
    # 0으로 나누는 경우 런타임 에러가 발생해서 예외처리를 해주어야 합니다.
    for i in range(1, N+1):
        if total_people == 0:
            failure[i] = 0
        else:
            failure[i] = stopped[i] / total_people
            total_people -= stopped[i]
						
    for key, val in sorted(failure.items(), key=lambda x: (-x[1], x[0])):
        result.append(key)
    return result