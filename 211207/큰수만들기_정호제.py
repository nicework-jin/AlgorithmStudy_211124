'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.3MB)
테스트 6 〉	통과 (2.68ms, 10.4MB)
테스트 7 〉	통과 (4.90ms, 11MB)
테스트 8 〉	통과 (14.94ms, 11.6MB)
테스트 9 〉	통과 (9.10ms, 15.6MB)
테스트 10 〉	통과 (81.73ms, 15.4MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
'''
from collections import deque

def solution(number, k):
    answer = [number[0]]
    que = deque(number[1:])
    
    while que:        
        if k > 0:
            new_num = que.popleft()
            while True:
                if not answer or answer[-1] >= new_num or k == 0:
                    break
                answer.pop()
                k -= 1
            answer.append(new_num)
                
        else:
            answer.extend(que)
            que = []
    
    return ''.join(answer[:len(answer)-k])