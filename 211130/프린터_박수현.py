"""
https://programmers.co.kr/learn/courses/30/lessons/42587

정확성  테스트
테스트 1 〉	통과 (0.16ms, 10.3MB)
테스트 2 〉	통과 (1.24ms, 10.3MB)
테스트 3 〉	통과 (0.14ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.13ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (0.85ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.14ms, 10.2MB)
테스트 11 〉	통과 (0.85ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.52ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
테스트 17 〉	통과 (1.08ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.71ms, 10.2MB)
테스트 20 〉	통과 (0.11ms, 10.2MB)

조건
- 중요도 높은 문서를 먼저 인쇄
1. 1<= 대기 목록 문서 수 <=100
2. 중요도는 숫자가 클수록 중요
3. location은 0부터 시작

알고리즘
1. 대기목록 가장 앞 문서(J)를 대기목록에서 꺼냄
2. 나머지 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
J를 대기목록의 가장 마지막에 넣는다.
3. 그렇지 않으면 J를 인쇄
4. 만약 J의 위치가 location과 같다면 반복문 종료

input: 중요도 배열, 인쇄 요청 문서의 위치(int)
output: 요청 문서가 몇 번째로 인쇄되는지 리턴(int)
"""
from collections import deque


def solution(priorities, location):
    print_num = 1
    q = deque()
    for idx, priority in enumerate(priorities):
        q.append([priority, idx])

    while q:
        # 1
        J = q.popleft()
        # 2
        if q and max(q)[0] > J[0]:
            q.append(J)
        # 3
        else:
            # 4
            if J[1] == location:
                break
            print_num += 1
    return print_num
