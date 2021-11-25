"""
https://programmers.co.kr/learn/courses/30/lessons/42839

테스트 1 〉	통과 (0.15ms, 10.4MB)
테스트 2 〉	통과 (181.11ms, 10.5MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (6.43ms, 10.4MB)
테스트 5 〉	통과 (5.41ms, 11.6MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.10ms, 10.5MB)
테스트 8 〉	통과 (5.44ms, 11.6MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (2287.68ms, 10.5MB)
테스트 11 〉	통과 (78.18ms, 10.4MB)
테스트 12 〉	통과 (0.59ms, 10.5MB)
"""
from itertools import permutations


def is_prime_number(n):
    if n == 0 or n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def solution(numbers):
    num_list = list()
    for n in range(1, len(numbers) + 1):
        num_list.extend(map(lambda x: int(''.join(x)), list(permutations(numbers, n))))

    cnt = 0
    for x in set(num_list):
        if is_prime_number(x):
            cnt += 1
    return cnt


if __name__ == "__main__":
    # 3
    numbers = "17"

    # 2
    numbers = "011"

    print(solution(numbers))