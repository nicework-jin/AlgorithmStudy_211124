'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.3MB)
테스트 11 〉	통과 (0.17ms, 10.3MB)
테스트 12 〉	통과 (1.64ms, 10.3MB)
테스트 13 〉	통과 (0.38ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
테스트 16 〉	통과 (0.05ms, 10.3MB)
테스트 17 〉	통과 (0.05ms, 10.3MB)
테스트 18 〉	통과 (5.60ms, 10.9MB)
테스트 19 〉	통과 (3.82ms, 10.4MB)
테스트 20 〉	통과 (6.64ms, 11MB)
테스트 21 〉	통과 (1.97ms, 10.4MB)
테스트 22 〉	통과 (2.52ms, 10.4MB)
테스트 23 〉	통과 (0.06ms, 10.3MB)
테스트 24 〉	통과 (5.66ms, 10.3MB)
테스트 25 〉	통과 (4.63ms, 10.5MB)
테스트 26 〉	통과 (3.32ms, 10.4MB)
테스트 27 〉	통과 (0.35ms, 10.3MB)
테스트 28 〉	통과 (0.42ms, 10.3MB)
'''
from itertools import combinations
from collections import defaultdict

def solution(relation):
    key_lst = [i for i in range(len(relation[0]))]
    key_combi = []
    key_candi = []
    uniq_set = defaultdict(set)
    answer = defaultdict(int)
    
    # 0, 1, 2, 3 이 index가 됨, 모든 경우의 수가 전체 후보가 됨
    for i in range(1, len(relation[0]) + 1):
        key_combi += list(combinations(key_lst, i))
    
    # index의 경우의 수에 따라 값드을 set에 추가
    for row in relation:
        for key in key_combi:
            tmp = ''
            for k in key:
                tmp += row[k]
            uniq_set[key].add(tmp)
    
    # 유일성 확인: 경우의 수들이 사람 수와 같은지 확인
    for key in uniq_set.keys():
        if len(uniq_set[key]) == len(relation):
            key_candi.append(key)
    
    # 최소성 확인: 성분이 key_candi와 answer에 없는 경우 선택
    for key in key_candi:
        break_trig = False
        for i in range(1, len(key) + 1):
            for tmp in combinations(key, i):
                if tmp in key_candi and tmp in answer:
                    break_trig = True
                    break
            if break_trig:
                break 
        else:
            answer[key] += 1

    return len(answer)