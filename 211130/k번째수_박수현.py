"""
https://programmers.co.kr/learn/courses/30/lessons/42748

정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)

조건
input: array 배열, commands의 [[i,j,k],...] 배열
output: 각 command의 k번째 수 배열

알고리즘
1. i부터 j까지 배열 자르기
2. 1의 배열 정렬
3. 2의 배열의 k번째 수 구하기
"""


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer
