"""
https://programmers.co.kr/learn/courses/30/lessons/72412

정확성  테스트
테스트 1 〉	통과 (0.18ms, 10.5MB)
테스트 2 〉	통과 (0.20ms, 10.4MB)
테스트 3 〉	통과 (0.32ms, 10.4MB)
테스트 4 〉	통과 (1.87ms, 10.5MB)
테스트 5 〉	통과 (2.43ms, 10.6MB)
테스트 6 〉	통과 (4.06ms, 10.5MB)
테스트 7 〉	통과 (4.45ms, 10.8MB)
테스트 8 〉	통과 (28.68ms, 11.5MB)
테스트 9 〉	통과 (29.74ms, 11.6MB)
테스트 10 〉	통과 (29.31ms, 11.7MB)
테스트 11 〉	통과 (2.56ms, 10.6MB)
테스트 12 〉	통과 (3.83ms, 10.5MB)
테스트 13 〉	통과 (3.82ms, 10.7MB)
테스트 14 〉	통과 (15.87ms, 11MB)
테스트 15 〉	통과 (15.92ms, 10.8MB)
테스트 16 〉	통과 (2.39ms, 10.5MB)
테스트 17 〉	통과 (7.11ms, 10.4MB)
테스트 18 〉	통과 (19.50ms, 11MB)
효율성  테스트
테스트 1 〉	통과 (587.02ms, 42.5MB)
테스트 2 〉	통과 (649.57ms, 42.4MB)
테스트 3 〉	통과 (696.11ms, 42.5MB)
테스트 4 〉	통과 (689.69ms, 42.7MB)

조건
- 각 조건에 해당하는 사람들의 숫자를 배열에 담아 리턴하라
1. info = 개발 언어, 직군, 경력, 소울푸드, 점수로 이뤄짐
2. 쿼리에서 각 원소는 -가 될 수 있음

알고리즘
1. 정수 앞에 있는 문자열을 분리
2. 0개~4개(총 4개의 항목이므로)의 조합으로 생성
3. 해당 조합을 key로 가지고 val은 점수로 가지는 딕셔너리 설정
4. 3의 딕셔너리를 점수로 오름차순 정렬
5. 쿼리의 불필요한 and, - 요소 제거
6. 해당 쿼리값을 key로 가지는 딕셔너리를 3에서 찾고 점수를 얻음
7. 6의 점수가 쿼리의 점수보다 높은지 이분 탐색으로 탐색
(점수에 따라 오름차순 정렬이므로 한 요소를 찾으면 그 뒷 요소들은 모두 만족한다.)
8. 7을 만족하면 만족하는 개수들을 정답에 추가

"""
from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        # 점수 앞에 있는 문자열
        key = info[:-1]
        # 점수
        val = int(info[-1])
        for i in range(5):
            # 하나의 info에서 0개~4개의 원소를 가지는 조합 만들기
            for combi in combinations(key, i):
                combi_key = ''.join(combi)
                info_dict[combi_key].append(val)
                
    for key in info_dict.keys():
        # lower bound 사용하기 위해 점수를 오름차순으로 정렬
        info_dict[key].sort()
    
    
    for query in queries:
        query = query.split()
        q_score = int(query[-1])
        query = query[:-1]
        
        # and와 -를 제거하고 하나의 문자열로 만듦 = backendjuniorpizza
        for i in range(3):
            query.remove('and')
        
        while '-' in query:
            query.remove('-')
            
        # 리스트를 문자열로
        q_key = ''.join(query)
        if q_key in info_dict:
            scores = info_dict[q_key]
            # 이분 탐색으로 쿼리 점수보다 높은 요소 파악
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - end)
        else:
            answer.append(0)
    return answer