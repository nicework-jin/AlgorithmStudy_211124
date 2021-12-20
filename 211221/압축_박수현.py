"""
https://programmers.co.kr/learn/courses/30/lessons/17684

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (12.88ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (43.94ms, 10.3MB)
테스트 7 〉	통과 (11.97ms, 10.2MB)
테스트 8 〉	통과 (25.78ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (25.95ms, 10.3MB)
테스트 11 〉	통과 (13.22ms, 10.3MB)
테스트 12 〉	통과 (40.38ms, 10.2MB)
테스트 13 〉	통과 (89.74ms, 10.3MB)
테스트 14 〉	통과 (85.05ms, 10.3MB)
테스트 15 〉	통과 (88.56ms, 10.3MB)
테스트 16 〉	통과 (42.01ms, 10.3MB)
테스트 17 〉	통과 (37.51ms, 10.2MB)
테스트 18 〉	통과 (3.08ms, 10.3MB)
테스트 19 〉	통과 (6.29ms, 10.3MB)
테스트 20 〉	통과 (28.13ms, 10.3MB)

조건
- 압축한 후의 사전 색인 번호를 배열로 출력하라
1. 영문 대문자만 처리

알고리즘
1. 길이가 1인 모든 단어를 포함하는 사전 생성
2. 사전 에서 입력과 일치하는 가장 긴 문자열 w 찾기
3. w에 해당하는 사전의 색인 번호를 출력, 입력에서 w 제거
4. 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록
5. 단계 2로 돌아감

"""
from collections import defaultdict
def solution(msg):
    answer = []
    # 1
    dic = {}
    for i in range(1,27):
        dic[chr(64+i)] = i
    start = 0
    end = len(msg)
    while True:
        # 2: 가장 긴 문자열 w 찾기, 범위를 가장 긴 문자열에서 좁히면 확실하게 사전에 있는 최대 배열이므로 반대의 경우보다 예외 처리에 편하다.
        w = msg[start:end]
        if w in dic.keys():
            # 3: 사전에 있는 색인 번호 출력
            answer.append(dic[w])
            # 4-1: 만약 모든 문자를 탐색했다면 정답 리턴
            if end == len(msg):
                return answer
            # 4-2: 다음 글자가 남아 있다면 w+c를 사전에 등록
            c = msg[end]
            dic[w+c] = len(dic) + 1
            # w 뒤에 있는 문자열부터 탐색해야 하므로 시작과 끝 초기화
            start += len(w)
            end = len(msg)
        else:
            end -= 1
            