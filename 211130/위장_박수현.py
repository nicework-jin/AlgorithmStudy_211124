"""
https://programmers.co.kr/learn/courses/30/lessons/42578

정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.02ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
테스트 28 〉	통과 (0.02ms, 10.1MB)

조건
1. [의상 이름, 종류] 배열이 주어짐
2. 1<=의상 수<=30
3. 같은 이름의 의상 없음
4. 하루에 최소 한 개의 의상은 입는다.

알고리즘
1. cloth_dic 생성, "종류: [옷 이름, 옷이름2,...]"
2. cloth_dic 종류마다 for 문
3. answer * (종류 개수 + 1)
4. 모두 안 입는 경우 제외
"""
from collections import defaultdict


def solution(clothes):
    answer = 1
    # 1
    cloth_dic = defaultdict(list)
    for name, type in clothes:
        cloth_dic[type].append(name)
    # 2
    for type, cloth in cloth_dic.items():
        # 3
        answer *= len(cloth) + 1
    # 4
    return answer - 1
