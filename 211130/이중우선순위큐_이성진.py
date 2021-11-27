"""
https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
"""

import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        # push 조건
        if operation[0] == 'I':
            v = int(operation[1:])
            heapq.heappush(min_heap, v)
            heapq.heappush(max_heap, -v)

        # pull 조건
        else:
            # 큐가 비었을 때
            if not min_heap:
                pass
            # 최대값 삭제
            elif operation[2:] == '1':
                mx_v = -heapq.heappop(max_heap)
                min_heap.remove(mx_v)
            # 최솟값 삭제
            else:
                mn_v = heapq.heappop(min_heap)
                max_heap.remove(-mn_v)
    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]


if __name__ == "__main__":
    # [0,0]
    operations = ["I 16", "D 1"]

    # [16, 16]
    operations = ["D 1", "I 16"]

    # [7,5]
    # operations = ["I 7", "I 5", "I -5", "D -1"]

    # [0, 0]
    # operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    print(solution(operations))
