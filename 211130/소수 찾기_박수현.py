"""
https://programmers.co.kr/learn/courses/30/lessons/42839



"""
"""
조건
- 숫자를 조합하여 만들 수 있는 소수 개수 구하기
input: 종이 조각에 들어있는 숫자(string)
output: 조합으로 만들 수 있는 소수 개수(int)

알고리즘:
1. (1~숫자 개수) 범위 내에서 조합할 수 있는 수를 모두 구함
2. 제곱근으로 중앙에 위치한 약수를 구하고, 그 이하의 수들이 소수인지 판별
3. 소수일 때마다 +1을 하고 합계 리턴
"""


# 2




from itertools import permutations
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
