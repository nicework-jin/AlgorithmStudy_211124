"""
https://programmers.co.kr/learn/courses/30/lessons/42888

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 9.99MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.62ms, 10.4MB)
테스트 6 〉	통과 (0.64ms, 10.3MB)
테스트 7 〉	통과 (0.54ms, 10.3MB)
테스트 8 〉	통과 (0.67ms, 10.3MB)
테스트 9 〉	통과 (0.75ms, 10.4MB)
테스트 10 〉	통과 (0.65ms, 10.4MB)
테스트 11 〉	통과 (0.36ms, 10.3MB)
테스트 12 〉	통과 (0.36ms, 10.2MB)
테스트 13 〉	통과 (0.65ms, 10.4MB)
테스트 14 〉	통과 (0.84ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.4MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (0.05ms, 10.3MB)
테스트 19 〉	통과 (0.69ms, 10.5MB)
테스트 20 〉	통과 (0.50ms, 10.2MB)
테스트 21 〉	통과 (0.49ms, 10.2MB)
테스트 22 〉	통과 (0.54ms, 10.3MB)
테스트 23 〉	통과 (0.73ms, 10.4MB)
테스트 24 〉	통과 (0.76ms, 10.4MB)
테스트 25 〉	통과 (98.17ms, 44.9MB)
테스트 26 〉	통과 (102.57ms, 49.3MB)
테스트 27 〉	통과 (117.56ms, 52.8MB)
테스트 28 〉	통과 (116.85ms, 54.8MB)
테스트 29 〉	통과 (106.72ms, 54.8MB)
테스트 30 〉	통과 (75.17ms, 44.6MB)
테스트 31 〉	통과 (88.16ms, 52.4MB)
테스트 32 〉	통과 (77.14ms, 47.5MB)

조건
- 모든 기록 처리 후, 방을 개설한 사람이 보게 되는 메세지 리턴
1. 첫 단어는 Enter, Leave, Change 중 하나
2. 유저 아이디는 대소문자를 구별

알고리즘
1. Enter: 닉네임 새로 저장(다시 들어왔는지 체크, 이전 이름 바꿈)
2. Leave: 나감
3. Change: 이전 이름 변경
"""
def solution(records):
    answer = []
    message = []
    user = {}
    for record in records:
        record = record.split()
        command, uid = record[0], record[1]
        if command == "Enter":
            user[uid] = record[2]
            message.append([command, uid])
        elif command == "Leave":
            message.append([command, uid])
        elif command == "Change":
            user[uid] = record[2]
            
    for m in message:
        if m[0] == "Enter":
            answer.append(user[m[1]]+"님이 들어왔습니다.")
        else:
            answer.append(user[m[1]]+"님이 나갔습니다.")
    return answer