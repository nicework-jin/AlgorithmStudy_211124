"""
https://programmers.co.kr/learn/courses/30/lessons/42895

정확성  테스트
테스트 1 〉	통과 (0.43ms, 10.5MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (9.11ms, 12.4MB)
테스트 5 〉	통과 (5.23ms, 11.5MB)
테스트 6 〉	통과 (0.13ms, 10.4MB)
테스트 7 〉	통과 (0.12ms, 10.4MB)
테스트 8 〉	통과 (7.18ms, 11.9MB)
테스트 9 〉	통과 (0.01ms, 10.4MB)

조건
- N과 사칙연산을 사용해서 number를 표현할 때, N 사용횟수의 최솟값
1. 최솟값이 8보다 크면 -1 리턴
2. 나누기 연산에서 나머지는 무시

알고리즘
1. n을 1~8번 사용하는 사칙연산
2. i-1번 배열과 i번 배열의 연산값을 배열에 추가
3. n을 i번 이어붙인 문자열을 추가
3. 배열에 number가 있다면 연산값 리턴
4. 8번 초과인 경우 -1 리턴 
"""


def solution(N, number):
    dp = [[]]
    # 1
    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    # 2
                    temp.append(k + l)
                    if k - l >= 0:
                        temp.append(k - l)
                    temp.append(k * l)
                    if l != 0 and k != 0:
                        temp.append(k // l)
        # 3
        temp.append(int(str(N) * i))
        if number in temp:
            return i
        dp.append(list(set(temp)))
    # 4
    return -1
