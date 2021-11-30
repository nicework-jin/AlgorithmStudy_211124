"""
https://programmers.co.kr/learn/courses/30/lessons/42628

정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
"""

import heapq


def solution(operations):
    heap = []
    for op in operations:
        order, num = op.split()[0], int(op.split()[1])
        if order == "I":
            heapq.heappush(heap, num)

        else:
            if heap:
                if num == 1:
                    idx = heap.index(heapq.nlargest(1, heap)[0])
                    heap.pop(idx)
                else:
                    heapq.heappop(heap)

    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else:
        return [0, 0]
