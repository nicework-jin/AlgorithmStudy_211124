"""
https://programmers.co.kr/learn/courses/30/lessons/42883

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.4MB)
테스트 5 〉	통과 (0.15ms, 10.3MB)
테스트 6 〉	통과 (2.51ms, 10.3MB)
테스트 7 〉	통과 (8.12ms, 10.7MB)
테스트 8 〉	통과 (16.18ms, 10.7MB)
테스트 9 〉	통과 (31.03ms, 13.6MB)
테스트 10 〉	통과 (89.79ms, 13.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)

조건
- k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수 구하기
1. 1<=k<number 자릿수

알고리즘
1. stack 생성
2. 문자열 모든 원소 탐색
3. 스택 마지막 값보다 넣으려는 값이 클 때 반복
3-1. 뺄 수 있는 수가 남았다면 스택 값 제거
4. 3 종료 후 원소 삽입
5. 뺄 수 있는 수가 더 남았다면 뒤에서부터 제거(앞은 고려해서 넣은 수일 가능성 높음)

"""


def solution(number, k):
    answer = ''
    # 1
    stack = []
    # 2
    for n in number:
        # 3 스택 마지막 값보다 넣으려는 값이 클 때
        while stack and n > stack[-1]:
            # 3-1: 뺄 수 있는 수가 남았다면 스택 값 제거
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        # 4: 더 이상 뺄 수 없다면
        stack.append(n)

    # 5: 뺄 수 있는 수가 더 남았다면
    if k > 0:
        for i in range(k):
            stack.pop()
    return ''.join(stack)
