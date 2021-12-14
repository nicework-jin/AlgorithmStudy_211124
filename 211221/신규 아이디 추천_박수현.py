"""
https://programmers.co.kr/learn/courses/30/lessons/72410

정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.4MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.05ms, 10.2MB)
테스트 18 〉	통과 (0.07ms, 10.3MB)
테스트 19 〉	통과 (0.14ms, 10.3MB)
테스트 20 〉	통과 (0.07ms, 10.3MB)
테스트 21 〉	통과 (0.10ms, 10.3MB)
테스트 22 〉	통과 (0.07ms, 10.3MB)
테스트 23 〉	통과 (0.12ms, 10.3MB)
테스트 24 〉	통과 (0.11ms, 10.2MB)
테스트 25 〉	통과 (0.12ms, 10.2MB)
테스트 26 〉	통과 (0.12ms, 10.3MB)

조건
- 7단계를 거쳐 추천 아이디를 리턴
1. new_id는 대소문자, 숫자, 특수문자로 구성
"""
def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
            
    #3단계
    while '..' in answer:
        answer = answer.replace('..','.')
        
    #4단계
    if answer[0] == '.' and len(answer) >= 2:
        answer=answer[1:]
            
    if answer[-1] == '.':
        answer=answer[:-1]
        
    #5단계
    if answer == "":
        answer = "a"
    
    #6단계
    if len(answer) >=16 :
        answer=answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    
    #7단계
    while len(answer)<3:
        answer+=answer[-1]
            
    return answer