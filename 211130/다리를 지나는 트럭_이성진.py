"""
https://programmers.co.kr/learn/courses/30/lessons/42583

테스트 1 〉	통과 (0.45ms, 10.3MB)
테스트 2 〉	통과 (6.63ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (5.33ms, 10.3MB)
테스트 5 〉	통과 (63.45ms, 10.3MB)
테스트 6 〉	통과 (14.80ms, 10.4MB)
테스트 7 〉	통과 (0.43ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (2.00ms, 10.3MB)
테스트 10 〉	통과 (0.17ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.28ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.53ms, 10.3MB)
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    bridge = deque([0]) * (bridge_length + 1)
    curr_bridge_weight = 0

    cnt = 1
    while truck_weights or curr_bridge_weight > 0:
        if truck_weights and curr_bridge_weight + truck_weights[-1] <= weight:
            w = truck_weights.pop()
            bridge[0] = w
            curr_bridge_weight += w

        cnt += 1
        bridge.rotate()

        if bridge[-1] != 0:
            curr_bridge_weight -= bridge[-1]
            bridge[-1] = 0
    return cnt


if __name__ == "__main__":
    # 8
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    # 101
    bridge_length = 100
    weight = 100
    truck_weights = [10]

    # 110
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]

    print(solution(bridge_length, weight, truck_weights))