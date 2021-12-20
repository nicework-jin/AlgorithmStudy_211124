'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.06ms, 10.4MB)
테스트 4 〉	통과 (0.09ms, 10.3MB)
테스트 5 〉	통과 (0.92ms, 10.5MB)
테스트 6 〉	통과 (1.49ms, 10.5MB)
테스트 7 〉	통과 (1.32ms, 10.5MB)
테스트 8 〉	통과 (0.94ms, 10.5MB)
테스트 9 〉	통과 (1.10ms, 10.7MB)
테스트 10 〉	통과 (1.06ms, 10.6MB)
테스트 11 〉	통과 (0.94ms, 10.4MB)
테스트 12 〉	통과 (0.60ms, 10.4MB)
테스트 13 〉	통과 (0.96ms, 10.5MB)
테스트 14 〉	통과 (1.34ms, 10.7MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.12ms, 10.3MB)
테스트 18 〉	통과 (0.10ms, 10.4MB)
테스트 19 〉	통과 (1.05ms, 10.6MB)
테스트 20 〉	통과 (1.59ms, 10.4MB)
테스트 21 〉	통과 (0.71ms, 10.4MB)
테스트 22 〉	통과 (0.77ms, 10.4MB)
테스트 23 〉	통과 (1.09ms, 10.7MB)
테스트 24 〉	통과 (1.12ms, 10.6MB)
테스트 25 〉	통과 (116.15ms, 48MB)
테스트 26 〉	통과 (122.83ms, 53.9MB)
테스트 27 〉	통과 (141.38ms, 58.8MB)
테스트 28 〉	통과 (142.40ms, 61.6MB)
테스트 29 〉	통과 (140.57ms, 61.4MB)
테스트 30 〉	통과 (101.11ms, 49.3MB)
테스트 31 〉	통과 (117.29ms, 61.4MB)
테스트 32 〉	통과 (102.05ms, 53.3MB)
'''
from collections import defaultdict

def solution(record):
    answer, log = [], []
    name_dic = defaultdict(str)
    
    for event in record:
        event_lst = event.split()
        
        if event_lst[0] == 'Leave':
            status, ID = event.split()
        else:
            status, ID, name = event.split()
            
        if status == 'Enter':
            name_dic[ID] = name
            log.append("{}님이 들어왔습니다.".format(ID))
        elif status == 'Leave':
            log.append("{}님이 나갔습니다.".format(ID))
        else:
            name_dic[ID] = name
    
    for sentetnce in log:
        ID, tmp1, tmp2 = sentetnce.partition('님이')
        answer.append(name_dic[ID] + tmp1 + tmp2)
            
    return answer