"""
https://programmers.co.kr/learn/courses/30/lessons/42587

테스트 1 〉	통과 (0.34ms, 10.2MB)
테스트 2 〉	통과 (2.72ms, 10.3MB)
테스트 3 〉	통과 (0.17ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.47ms, 10.2MB)
테스트 7 〉	통과 (0.55ms, 10.1MB)
테스트 8 〉	통과 (3.43ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.28ms, 10.2MB)
테스트 11 〉	통과 (1.33ms, 10.2MB)
테스트 12 〉	통과 (0.08ms, 10.2MB)
테스트 13 〉	통과 (1.21ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.08ms, 10.2MB)
테스트 17 〉	통과 (2.24ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (1.65ms, 10.2MB)
테스트 20 〉	통과 (0.23ms, 10.3MB)
"""
from collections import deque


def solution(priorities, location):
    idx_priority_pairs = deque(map(lambda x: x, enumerate(priorities)))
    cnt = 0
    while True:
        if idx_priority_pairs[0][1] == max(idx_priority_pairs, key=lambda x: x[1])[1]:
            k, _ = idx_priority_pairs.popleft()
            cnt += 1
            if k == location:
                return cnt
        else:
            idx_priority_pairs.rotate(-1)


if __name__ == "__main__":
    # 1
    priorities = [2, 1, 3, 2]
    location = 2

    # 5
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
