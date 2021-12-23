"""
https://programmers.co.kr/learn/courses/30/lessons/60058

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.3MB)
테스트 16 〉	통과 (0.12ms, 10.3MB)
테스트 17 〉	통과 (0.12ms, 10.2MB)
테스트 18 〉	통과 (0.18ms, 10.3MB)
테스트 19 〉	통과 (0.25ms, 10.3MB)
테스트 20 〉	통과 (0.21ms, 10.3MB)
테스트 21 〉	통과 (0.19ms, 10.3MB)
테스트 22 〉	통과 (0.10ms, 10.3MB)
테스트 23 〉	통과 (0.18ms, 10.3MB)
테스트 24 〉	통과 (0.09ms, 10.3MB)
테스트 25 〉	통과 (0.15ms, 10.3MB)

조건
- 주어진 알고리즘을 수행해 올바른 괄호 문자열로 변환하여 리턴하라
1. 균형잡힌 괄호 문자열: '('와 ')'의 개수가 같음
2. 올바른 괄호 문자열: 1에 해당하며 괄호의 짝이 맞는 경우
3. 전체 문자열을 이루는 '('와 ')'의 개수는 항상 같음
"""
from collections import deque

# 2: 균형 잡힌 문자열로 분리
def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]

# 3: 올바른 괄호 문자열인지 체크
def check(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    # 1
    if not p:
        return ""
    # 2
    u, v = divide(p)
    # 3: 올바른 괄호 문자열이라면 v에 대해 1부터 수행
    if check(u):
        # 3-1: 수행한 문자열을 u에 이어 붙이고 반환
        return u + solution(v)
    
    # 3: 올바른 괄호 문자열이 아니라면
    else:
        # 4-1 ~ 4-3
        s = '('
        s += solution(v)
        s += ')'
        # 4-4: 첫, 마지막 문자 제거, 문자열 괄호 방향 뒤집어서 뒤에 붙이기
        for p in u[1:len(u)-1]:
            if p == '(':
                s += ')'
            else:
                s += '('
        return s
