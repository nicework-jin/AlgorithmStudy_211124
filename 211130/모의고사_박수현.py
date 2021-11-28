"""
https://programmers.co.kr/learn/courses/30/lessons/42840

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (3.06ms, 10.3MB)
테스트 8 〉	통과 (0.99ms, 10.3MB)
테스트 9 〉	통과 (5.35ms, 10.3MB)
테스트 10 〉	통과 (2.66ms, 10.3MB)
테스트 11 〉	통과 (5.89ms, 10.3MB)
테스트 12 〉	통과 (5.10ms, 10.3MB)
테스트 13 〉	통과 (0.55ms, 10.2MB)
테스트 14 〉	통과 (6.11ms, 10.3MB)

조건
1. 시험 최대 10000문제
2. 최고 득점자가 여럿일 경우 return 값 오름차순 정렬

input: 정답 배열
output: 가장 많이 맞힌 사람 배열

알고리즘
1. 각 수포자들의 정답 배열 생성(반복 제외)
2. answers와 각 수포자들의 정답 비교, 맞힌 갯수 저장
3. count 배열의 최대값과 같다면 idx 저장, idx를 순서대로 저장하는게 오름차순 
"""


def solution(answers):
    # 1
    sp_answer = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2,
                                   4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    count = [0, 0, 0]

    # 2
    for i in range(len(answers)):
        for j in range(3):
            length = len(sp_answer[j])
            if answers[i] == sp_answer[j][i % length]:
                count[j] += 1

    # 3
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)

    return answer
