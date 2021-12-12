"""
https://programmers.co.kr/learn/courses/30/lessons/43238

정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (3.61ms, 10.3MB)
테스트 4 〉	통과 (302.21ms, 14.2MB)
테스트 5 〉	통과 (414.25ms, 14.3MB)
테스트 6 〉	통과 (271.31ms, 14.2MB)
테스트 7 〉	통과 (520.18ms, 14.2MB)
테스트 8 〉	통과 (506.39ms, 14.2MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)

제한사항
- 모든 사람이 심사를 받는데 걸리는 최소 시간 구하기
1. 한 심사대에서 한 명만 심사 가능
2. 1 <= 기다리는 사람 수, 걸리는 시간 <= 1,000,000,000

알고리즘
1. 최소 시간: 1분, 최대 시간: (가장 오래 걸리는 시간) * 사람 수
2. 최소 시간이 최대 시간 이하일 때 반복
3. 중간값 구하기
4. 가능한 사람 수 += 중간값 // times 배열값
5-1. 가능한 사람 >= n : right = mid
5-2. 가능한 사람 < n : left = mid + 1
"""

def solution(n, times):
    answer = 0
    # 1
    left = 1
    right = max(times) * n
    
    # 2
    while left < right:
        # 3
        mid = (left + right) // 2
        # 4
        total = 0
        for t in times:
            total += mid // t
        # 5-1
        if total >= n:
            right = mid
        # 5-2
        else:
            left = mid + 1
    answer = left
    return answer