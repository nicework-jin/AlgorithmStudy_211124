'''
정확성  테스트
테스트 1 〉	통과 (1.42ms, 10.3MB)
테스트 2 〉	통과 (1.04ms, 10.2MB)
테스트 3 〉	통과 (1.00ms, 10.3MB)
테스트 4 〉	통과 (0.95ms, 10.3MB)
테스트 5 〉	통과 (0.53ms, 10.2MB)
테스트 6 〉	통과 (0.32ms, 10.2MB)
테스트 7 〉	통과 (0.47ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.95ms, 10.2MB)
테스트 11 〉	통과 (0.85ms, 10.2MB)
테스트 12 〉	통과 (0.70ms, 10.3MB)
테스트 13 〉	통과 (0.91ms, 10.4MB)
테스트 14 〉	통과 (1.18ms, 10.3MB)
테스트 15 〉	통과 (0.13ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (15.45ms, 10.7MB)
테스트 2 〉	통과 (15.10ms, 10.8MB)
테스트 3 〉	통과 (12.29ms, 10.7MB)
테스트 4 〉	통과 (15.36ms, 10.8MB)
테스트 5 〉	통과 (13.41ms, 10.6MB)
'''
from collections import deque

def solution(people, limit):
    answer = 0
    weight = 0
    people.sort(reverse = True)
    que = deque(people)
    
    while que:
        
        if limit >= que[0] + weight:
            weight += que.popleft()
        elif limit >= que[-1] + weight:
            weight += que.pop()
        else:
            answer += 1
            weight = 0
        
    return answer + 1