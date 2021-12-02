"""
https://programmers.co.kr/learn/courses/30/lessons/42862

테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
"""


def solution(n, lost, reserve):
    # 체육복을 몇 개씩 가지고 있는지?
    num = [1] * n  # 학생번호 = 인덱스 - 1
    for i in range(n):
        if i+1 in lost:
            num[i] -= 1

        if i+1 in reserve:
            num[i] += 1

    # # 왼쪽 친구부터 빌려주고, 없으면 오른쪽 친구
    for i in range(n):
        if num[i] < 2:
            continue

        if i > 0 and num[i-1] == 0:
            num[i] -= 1
            num[i-1] += 1
        elif i < n-1 and num[i+1] == 0:
            num[i] -= 1
            num[i+1] += 1
        else:
            pass
    return n - num.count(0)


if __name__ == "__main__":
    # 5
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]

    # 4
    n = 5
    lost = [2, 4]
    reserve = [3]

    # 2
    n = 3
    lost = [3]
    reserve = [1]

    print(solution(n, lost, reserve))