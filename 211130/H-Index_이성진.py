"""
https://programmers.co.kr/learn/courses/30/lessons/42747

테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.4MB)
테스트 6 〉	통과 (0.11ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.12ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.11ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.2MB)
테스트 15 〉	통과 (0.11ms, 10.4MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
"""


def solution(citations):
    # [0, 1, 3, 5, 6]
    citations.sort()
    length = len(citations)

    # 0 <= h_idx <= length 이므로
    for over in range(length):
        if (under := length - over) <= citations[over]:
            return under
    return 0


if __name__ == "__main__":
    # h: 1 ==> 4, 1
    # h: 2 ==> 3, 2
    # h: 3 ==> 3, 2
    # 3
    citations = [3, 0, 6, 1, 5]

    # h: 1 ==> 3, 0
    # h: 2 ==> 2, 1
    # h: 3 ==> 1, 2
    # 3
    # citations = [1, 2, 3]
    print(solution(citations))