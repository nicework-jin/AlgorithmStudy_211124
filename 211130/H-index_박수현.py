"""
https://programmers.co.kr/learn/courses/30/lessons/42747

정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.2MB)
테스트 6 〉	통과 (0.10ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.12ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.10ms, 10.2MB)
테스트 14 〉	통과 (0.10ms, 10.4MB)
테스트 15 〉	통과 (0.17ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)

조건
1. 1 <= citations 길이 <= 1000
2. 0 <= h 인덱스 크기 <= 10000

알고리즘
1. citations 내림차순 정렬(최대값을 구하기 위함)
2. 내림차순 후 현 idx = 현재 수 앞에 있는 수의 갯수
= 원배열에서 현재 수 뒤에 위치한 수의 갯수
3. 2번의 idx >= citation이라면 최대값인 h가 된다.
4. 모든 수가 3에 해당하지 않는다면 현재 배열의 길이보다 원소의 값이 모두 큰 것이므로 현재 배열의 길이 리턴
"""


def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        # 현재 수 앞에 idx개만큼 있음, idx가 citation편 이상이면 citation이 최대값인 h가 되는 것
        if idx >= citation:
            return idx

    return len(citations)
