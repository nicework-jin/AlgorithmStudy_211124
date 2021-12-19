"""
https://programmers.co.kr/learn/courses/30/lessons/42890

정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.3MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.18ms, 10.3MB)
테스트 10 〉	통과 (0.43ms, 10.3MB)
테스트 11 〉	통과 (0.42ms, 10.3MB)
테스트 12 〉	통과 (13.93ms, 10.3MB)
테스트 13 〉	통과 (1.05ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.3MB)
테스트 16 〉	통과 (0.09ms, 10.3MB)
테스트 17 〉	통과 (0.09ms, 10.3MB)
테스트 18 〉	통과 (24.55ms, 10.6MB)
테스트 19 〉	통과 (15.79ms, 10.3MB)
테스트 20 〉	통과 (19.47ms, 10.6MB)
테스트 21 〉	통과 (5.60ms, 10.6MB)
테스트 22 〉	통과 (3.72ms, 10.3MB)
테스트 23 〉	통과 (0.12ms, 10.2MB)
테스트 24 〉	통과 (19.40ms, 10.3MB)
테스트 25 〉	통과 (21.69ms, 10.5MB)
테스트 26 〉	통과 (16.71ms, 10.3MB)
테스트 27 〉	통과 (1.19ms, 10.3MB)
테스트 28 〉	통과 (0.95ms, 10.4MB)

조건
- 후보 키의 최대 개수를 구하라
1. 후보키는 유일성 만족: 모든 튜플에 대해 유일하게 식별
2. 후보키는 최소성 만족: 요소 중 하나라도 제외하는 경우 유일성이 깨짐

알고리즘
1. column 인덱스에 대한 모든 조합 생성
2. 유일성 검사: 해당 col의 모든 요소를 저장한 배열의 원소가, 중복을 제거해도 전체 행의 수와 같은지
3. 최소성 검사: 2를 통과한 인덱스에 대해 왼쪽과 오른쪽 원소의 교집합이 왼쪽 원소일 때 유일성이 깨지므로 오른쪽 원소를 집합에서 제거
"""
from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    
    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range(col), i))
    # 유일성 검사
    unique = []
    for col in candidates:
        tmp = []
        for rel_row in relation:
            tmp.append(tuple(rel_row[i] for i in col))
            # 중복을 제거해도 모든 행의 데이터가 있을 때 유일성 만족
            if len(set(tmp)) == row:
                # 유일성 만족하는 컬럼 저장
                unique.append(col)
    
    # 최소성 검사
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            # 다음 요소들과의 교집합이 현 요소와 같다면 겹치는 것
            # ex, [(0,)(0,1)]이 있을 때 둘은 왼쪽 요소를 교집합으로 가진다.
            # (0,1)에서 0이 빠지면 유일성이 깨진다. 그러므로 최소성을 만족하지 못함. 집합에서 오른쪽 요소를 제거한다.
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                # 집합에서 해당 요소를 제거한다.
                answer.discard(unique[j])
    return len(answer)