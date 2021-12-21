'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (0.35ms, 10.2MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (1.88ms, 10.3MB)
테스트 9 〉	통과 (1.26ms, 10.4MB)
테스트 10 〉	통과 (1.56ms, 10.5MB)
테스트 11 〉	통과 (0.84ms, 10.4MB)
테스트 12 〉	통과 (0.97ms, 10.4MB)
테스트 13 〉	통과 (1.47ms, 10.5MB)
테스트 14 〉	통과 (0.91ms, 10.4MB)
테스트 15 〉	통과 (1.54ms, 10.5MB)
테스트 16 〉	통과 (0.35ms, 10.3MB)
테스트 17 〉	통과 (0.20ms, 10.4MB)
테스트 18 〉	통과 (0.09ms, 10.3MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.27ms, 10.3MB)
'''
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    menu_dic = defaultdict(int)
    course_dic = defaultdict(list)
    
    for i in course:
        for order in orders:
            order = sorted(order)
            for menu in combinations(order, i):
                menu_dic[''.join(menu)] += 1
                
    for menu, cnt in menu_dic.items():
        if cnt == 1:
            continue
        course_dic[len(menu)].append([menu, cnt])
    
    for i in course:
        course_dic[i].sort(key = lambda x: -x[1])
        
        if not course_dic[i]:
            continue
        
        answer.append(course_dic[i][0][0])
        max_num = course_dic[i][0][1]

        for course_menu in course_dic[i][1:]:
            if course_menu[1] == max_num:
                answer.append(course_menu[0])
            else:
                break
                
    return sorted(answer)