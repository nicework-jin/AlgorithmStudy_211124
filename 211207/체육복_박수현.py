"""
https://programmers.co.kr/learn/courses/30/lessons/42862
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
조건
1. 바로 앞이나 뒤의 학생에게 빌려줄 수 있음
2. 여벌 있는 학생이 도난당할 수 있음(다른 학생에게 빌려줄 수 없음)
3. lost, reserve 배열은 unique
알고리즘
1. 전체 reserve 배열 탐색
2. 무조건 앞 학생에게 전달
- (3, 5)만 여벌이 있고 뒷 학생에게 전달한다고 했을 때 2번은 받을 수가 없다.
"""


def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for reserve in set_reserve:
        if reserve - 1 in set_lost:
            set_lost.remove(reserve - 1)
        elif reserve + 1 in set_lost:
            set_lost.remove(reserve + 1)

    return n - len(set_lost)
