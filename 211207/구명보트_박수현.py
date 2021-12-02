"""
https://programmers.co.kr/learn/courses/30/lessons/42885

정확성  테스트
테스트 1 〉	통과 (0.84ms, 10.4MB)
테스트 2 〉	통과 (0.62ms, 10.3MB)
테스트 3 〉	통과 (0.60ms, 10.2MB)
테스트 4 〉	통과 (0.54ms, 10.2MB)
테스트 5 〉	통과 (0.30ms, 10.2MB)
테스트 6 〉	통과 (0.18ms, 10.3MB)
테스트 7 〉	통과 (0.31ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.57ms, 10.2MB)
테스트 11 〉	통과 (0.49ms, 10.3MB)
테스트 12 〉	통과 (0.44ms, 10.3MB)
테스트 13 〉	통과 (0.56ms, 10.3MB)
테스트 14 〉	통과 (0.70ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (8.65ms, 10.6MB)
테스트 2 〉	통과 (8.50ms, 10.3MB)
테스트 3 〉	통과 (8.40ms, 10.5MB)
테스트 4 〉	통과 (9.45ms, 10.6MB)
테스트 5 〉	통과 (8.62ms, 10.4MB)

조건
1. 한 번에 2명 탈 수 있음
2. limit = 무게 제한
3. 가장 적은 구명보트 사용

알고리즘
1. 무게별로 정렬
2. 가장 가벼운 사람과 가장 무거운 사람을 limit과 비교
- 남은 사람들 중 가장 가벼운데 무게가 초과 됨 = 두 번째부터도 역시 초과 되므로 고려할 필요가 없음
"""
def solution(people, limit):
    answer = 0
    # 1
    people.sort()
    start, end = 0, len(people) - 1
    # 2
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        answer += 1
        end -= 1
        
    return answer