"""
https://programmers.co.kr/learn/courses/30/lessons/42839

정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.4MB)
테스트 2 〉	통과 (2.28ms, 10.5MB)
테스트 3 〉	통과 (0.03ms, 10.5MB)
테스트 4 〉	통과 (0.53ms, 10.5MB)
테스트 5 〉	통과 (3.15ms, 10.8MB)
테스트 6 〉	통과 (0.03ms, 10.5MB)
테스트 7 〉	통과 (0.07ms, 10.5MB)
테스트 8 〉	통과 (3.12ms, 11MB)
테스트 9 〉	통과 (0.04ms, 10.5MB)
테스트 10 〉	통과 (5.43ms, 10.5MB)
테스트 11 〉	통과 (0.54ms, 10.5MB)
테스트 12 〉	통과 (0.18ms, 10.5MB)

조건
- 숫자를 조합하여 만들 수 있는 소수 개수 구하기
input: 종이 조각에 들어있는 숫자(string)
output: 조합으로 만들 수 있는 소수 개수(int)

알고리즘:
1. (1~숫자 개수) 범위 내에서 조합할 수 있는 수를 모두 구함
2. 제곱근으로 중앙에 위치한 약수를 구하고, 그 이하의 수들이 소수인지 판별
3. 소수일 때마다 +1을 하고 합계 리턴
"""
from itertools import permutations
# 2


def isPrime(n):
    if n in (0, 1):
        return False
    sqrt = n ** 0.5
    for i in range(2, int(sqrt) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    p = []
    # 1
    for i in range(1, len(numbers) + 1):
        print(list(permutations(numbers, i)))
        temp = list(map(int, map(''.join, permutations(numbers, i))))
        p.extend(temp)

    p = list(set(p))

    for n in p:
        if isPrime(n):
            answer += 1

    # 3
    return answer
