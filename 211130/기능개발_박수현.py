"""
https://programmers.co.kr/learn/courses/30/lessons/42586

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.4MB)

조건
1. 진도 100%일 때 반영
2. 뒤에 있는 기능 개발돼도 앞에 있는 기능 개발 배포때 같이 배포됨
3. 배포는 하루에 한 번
4. input: 배열 2개, progresses: 작업 진도, speeds: 개발 속도
5. output: 각 배포마다의 기능 수가 포함된 배열 return

알고리즘
1. (작업 진도, 개발 속도)의 튜플 생성 후 모든 원소 반복
2. 소요되는 날짜 구하기: day.append(math.ceil((100-progress) // speed))
3. day 길이만큼 반복
4. 투 포인터 사용: day[front] < day[i]일 때 배포 가능
4-1. i-front만큼 큐에 저장, front = i
5. 남은 날짜 저장: len(day) - front 
"""
from collections import deque
import math


def solution(progresses, speeds):
    day = []
    q = deque()
    # 1
    for progress, speed in zip(progresses, speeds):
        # 2
        day.append(math.ceil((100-progress) / speed))
    # 3
    front = 0
    for i in range(len(day)):
        # 4
        if day[front] < day[i]:
            # 4-1
            q.append(i-front)
            front = i
    # 5
    q.append(len(day) - front)
    return list(q)
