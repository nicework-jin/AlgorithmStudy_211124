"""
https://programmers.co.kr/learn/courses/30/lessons/42576

정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.27ms, 10.3MB)
테스트 4 〉	통과 (0.46ms, 10.4MB)
테스트 5 〉	통과 (0.43ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (35.78ms, 18MB)
테스트 2 〉	통과 (57.78ms, 22.2MB)
테스트 3 〉	통과 (73.92ms, 24.7MB)
테스트 4 〉	통과 (78.49ms, 26.3MB)
테스트 5 〉	통과 (79.28ms, 26.3MB)

조건
1. 동명이인 있음
2. completion이 participant보다 1 작음

알고리즘
1. 두 배열(parti, comple) 정렬
2. 순서대로 튜플 생성, 같지 않다면 false
3. 모두 같다면 마지막 parti가 정답
"""


def solution(participant, completion):
    # 1
    participant.sort()
    completion.sort()
    # 2: comp의 길이에 맞춰서 튜플이 생성됨
    for part, comp in zip(participant, completion):
        if part != comp:
            return part
    # 3: 모두 같다면 마지막 part가 미완주자
    return participant[-1]
