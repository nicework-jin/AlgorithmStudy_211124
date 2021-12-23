"""
https://programmers.co.kr/learn/courses/30/lessons/72411

정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.10ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (0.35ms, 10.3MB)
테스트 7 〉	통과 (0.22ms, 10.3MB)
테스트 8 〉	통과 (1.32ms, 10.3MB)
테스트 9 〉	통과 (1.18ms, 10.3MB)
테스트 10 〉	통과 (1.50ms, 10.7MB)
테스트 11 〉	통과 (0.80ms, 10.3MB)
테스트 12 〉	통과 (0.90ms, 10.4MB)
테스트 13 〉	통과 (1.41ms, 10.7MB)
테스트 14 〉	통과 (0.95ms, 10.4MB)
테스트 15 〉	통과 (1.28ms, 10.6MB)
테스트 16 〉	통과 (0.35ms, 10.3MB)
테스트 17 〉	통과 (0.21ms, 10.3MB)
테스트 18 〉	통과 (0.12ms, 10.3MB)
테스트 19 〉	통과 (0.05ms, 10.2MB)
테스트 20 〉	통과 (0.27ms, 10.3MB)

조건
- 가장 많이 같이 주문한 단품 메뉴를 코스 요리로 구성하고 리턴하라
1. 코스 요리는 최소 2가지 이상의 단품 메뉴, 최소 2명 이상의 손님이 주문했을 때 구성
2. 각 문자열은 대문자, 중복 문자 없음
3. course 배열은 자연수 오름차순
4. 코스 요리는 알파벳 오름차순 정렬

알고리즘
1. course의 각 원소에 대해 탐색
2. orders의 각 원소들을 course개씩 조합하여 저장
3. 2를 카운터를 이용해 개수를 저장한다.
4. 그 중 가장 많은 주문을 받은 2개 이상의 조합을 정답에 저장
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # 1
    for num in course:
        order_list = []
        # 2
        for order in orders:
            # "XY", "YX"의 경우 다르게 인식하므로 함께 카운트 될 수 있게 정렬
            combi = combinations(sorted(order), num)
            order_list.extend(list(map(''.join, combi)))
        # 3
        counter = Counter(order_list).most_common()
        for menu, cnt in counter:
            # 4: 주문 횟수가 2회 이상이며 가장 많은 주문 횟수와 같을 때
            if cnt != 1 and cnt == counter[0][1]:
                answer.append(menu)
    return sorted(answer)