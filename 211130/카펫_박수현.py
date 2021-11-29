"""
https://programmers.co.kr/learn/courses/30/lessons/42842

정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (54.56ms, 10.2MB)
테스트 4 〉	통과 (0.25ms, 10.2MB)
테스트 5 〉	통과 (0.61ms, 10.3MB)
테스트 6 〉	통과 (18.70ms, 10.2MB)
테스트 7 〉	통과 (69.85ms, 10.2MB)
테스트 8 〉	통과 (51.72ms, 10.2MB)
테스트 9 〉	통과 (64.80ms, 10.2MB)
테스트 10 〉	통과 (81.15ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)

조건
1. 가로*세로 = yellow+brown
2. 가로 길이 >= 세로 길이
input: 갈색, 노란색 (int)
output: [가로, 세로] (배열)

알고리즘
1. 전체 카펫 = yellow + brown
2. for문 통해서 세로 길이 확인
3. (i-2) * (a-2) = brown이라면 리턴
"""


def solution(brown, yellow):
    # 1
    sums = brown + yellow
    # 2
    for i in range(sums, 2, -1):
        if sums % i == 0:
            a = sums // i
            # 3
            if (a-2) * (i-2) == yellow:
                return [i, a]
