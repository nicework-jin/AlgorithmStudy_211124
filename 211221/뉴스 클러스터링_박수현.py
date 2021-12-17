"""
https://programmers.co.kr/learn/courses/30/lessons/17677

정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.67ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.25ms, 10.2MB)
테스트 11 〉	통과 (0.45ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.4MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)

조건
- (자카드 유사도 값 * 65536) 소수점 아래 버리고 정수부만 출력
1. 자카드 유사도 = 교집합 크기 / 합집합 크기
(예외: 모두 공집합인 경우 유사도 = 1)
2. 교집합 1의 경우: min(3,5) = 3개
3. 합집합 1의 경우: max(3,5) = 5개
4. 문자열 2글자씩 끊어서 원소로 만듦
4-1. 영문자만 유효, 대소문자 구분 없음

알고리즘
1. 각 문자열 2글자씩 조합을 만들어서 저장
2. 두 배열의 교집합 구하기(중복 원소 고려해야 함)
3. 두 배열의 합집합 구하기
"""
from itertools import permutations
import math

def str_to_list(s):
    l = []
    for i in range(len(s) - 1):
        if s[i:i+2].isalpha():
            l.append(s[i:i+2].lower())
    return l
    
def solution(str1, str2):
    list1 = str_to_list(str1)
    list2 = str_to_list(str2)
    # 중복 원소도 카운트 하기 때문에 둘 다 가지고 있는 경우 하나씩 삭제하면서
    # 중복 원소의 개수를 센다.
    inter = [list2.remove(x) for x in list1 if x in list2]
    union = list1 + list2
    
    if len(union) ==  0:
        answer = 1 * 65536
    else:
        answer = math.trunc((len(inter) / len(union)) * 65536)
    return answer