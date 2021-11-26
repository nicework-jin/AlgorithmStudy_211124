"""
https://programmers.co.kr/learn/courses/30/lessons/42583

정확성  테스트
테스트 1 〉	통과 (11.81ms, 10.3MB)
테스트 2 〉	통과 (1409.57ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (314.56ms, 10.3MB)
테스트 5 〉	통과 (9751.37ms, 10.3MB)
테스트 6 〉	통과 (1651.98ms, 10.3MB)
테스트 7 〉	통과 (6.00ms, 10.2MB)
테스트 8 〉	통과 (0.20ms, 10.3MB)
테스트 9 〉	통과 (5.38ms, 10.3MB)
테스트 10 〉	통과 (0.25ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.26ms, 10.3MB)
테스트 13 〉	통과 (1.81ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)

조건
1. 다리에는 bridge_length대 만큼 올라옴
2. weight 이하의 무게를 견딜 수 있음

알고리즘
1. on_bridge: bridge_length 만큼의 원소가 0인 배열 생성
2. on_bridge 원소가 없어질 때까지 반복
3. 남은 트럭이 있다면
3-1. 남은 트럭을 on_bridge에 넣을 수 있다면(합이 weight보다 적음) 삽입
3-2. 합이 weight 보다 크다면 0을 삽입(무게에 영향 없음)
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 1
    on_bridge = [0] * bridge_length

    # 2
    while on_bridge:
        answer += 1
        on_bridge.pop(0)
        # 3
        if truck_weights:
            # 3-1
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            # 3-2
            else:
                on_bridge.append(0)

    return answer
