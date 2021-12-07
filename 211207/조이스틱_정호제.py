'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
'''
def solution(name):
    
    alp_dic = {chr(alp): i for i, alp in enumerate(range(ord('A'), ord('Z') + 1))}
    alp_rev_dic = {chr(alp): 26 - i for i, alp in enumerate(range(ord('A'), ord('Z') + 1))}
    sum_alp = sum(min(alp_dic[alp], alp_rev_dic[alp]) for alp in name)
    
    chk_lst = []
    for i in range(len(name)):
        if i == 0:
            chk_lst.append(-1)
            continue
        if name[i] != 'A':
            chk_lst.append(i)
        else:
            chk_lst.append(-1)
    
    pos = 0
    dist = 0
    
    while True:
        cnt = -1
        for i in range(len(name)):
            cnt += 1
            fward_pos = (pos + i)%len(name)
            back_pos = (pos - i)%len(name)
            
            if chk_lst[fward_pos] != -1:
                pos = fward_pos
                break
            elif chk_lst[back_pos] != -1:
                pos = back_pos
                break
        else:
            break
            
        chk_lst[pos] = -1
        dist += cnt
        
    return sum_alp + dist