'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.4MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
'''
def solution(n, lost, reserve):
    student = [0 for _ in range(n+1)]
    skip = [0 for _ in range(n+1)]
    answer = n - len(lost)
    
    reserve.sort()
    
    for i in lost:
        student[i] = -1
    
    for res in reserve:
        if student[res] == -1:
            student[res] = 1
            skip[res] = 1
            answer += 1
    
    for res in reserve:            
        if skip[res] == 0 and res - 1 >= 0 and student[res - 1] == -1:
            student[res - 1] = 1
            answer += 1
        elif skip[res] == 0 and n >= res + 1 and student[res + 1] == -1:
            student[res + 1] = 1
            answer += 1
            
    # print(student)
    return answer