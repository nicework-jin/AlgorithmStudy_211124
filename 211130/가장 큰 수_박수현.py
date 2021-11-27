"""
https://programmers.co.kr/learn/courses/30/lessons/42746

정확성  테스트
테스트 1 〉	통과 (807.71ms, 23.3MB)
테스트 2 〉	통과 (239.22ms, 17.1MB)
테스트 3 〉	통과 (1282.26ms, 27.4MB)
테스트 4 〉	통과 (1.71ms, 10.5MB)
테스트 5 〉	통과 (637.35ms, 22MB)
테스트 6 〉	통과 (485.65ms, 20.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.5MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)

조건
input: 정수 배열
output: 가장 큰 수 리턴(string)

알고리즘
1. 정수를 문자열로 변경
2. 정수를 3번 반복하는 문자열 비교, 오름차순으로 변경
예: 666 101010 222라면 문자열은 앞글자부터 비교하므로
6>2>1
3. 문자열을 다시 정수로 변환한 뒤 다시 문자열로 리턴
000과 같은 경우를 고려함
"""


def solution(numbers):
    # 1
    numbers = list(map(str, numbers))
    # 2
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 3
    return str(int(''.join(numbers)))
