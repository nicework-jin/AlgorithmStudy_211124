"""
https://programmers.co.kr/learn/courses/30/lessons/17680

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (72.96ms, 17.6MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (0.22ms, 10.3MB)
테스트 16 〉	통과 (0.15ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.40ms, 10.3MB)
테스트 19 〉	통과 (0.56ms, 10.3MB)
테스트 20 〉	통과 (0.67ms, 10.2MB)

조건
- 캐시 크기에 따른 총 실행시간을 구하라
1. 각 도시 이름은 영문자로만 구성, 대소문자 구분 없음
2. LRU 알고리즘 사용(가장 최근에 사용하지 않은 것 삭제)
3. hit: 실행시간 1, miss: 5

알고리즘
- 가장 이전에 사용한 것을 삭제해야하므로 덱을 사용
1. 모두 소문자 변환
2-1. 이미 스택에 있다면 hit 처리, 해당 값 삭제
2-2. 스택에 없다면 miss 처리
3. 스택이 캐시 크기보다 작다면 앞에서부터 삭제(가장 이전에 사용된 거니까)
4. 해당 값 맨 뒤에 삽입
"""
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    stack = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in stack:
            stack.remove(city)
            answer += 1
        else:
            answer += 5
        if cacheSize <= len(stack):
            stack.popleft()
        stack.append(city)
        
    return answer