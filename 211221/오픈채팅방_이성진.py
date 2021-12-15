# https://programmers.co.kr/learn/courses/30/lessons/42888

"""

테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.68ms, 10.5MB)
테스트 6 〉	통과 (1.24ms, 10.7MB)
테스트 7 〉	통과 (0.64ms, 10.5MB)
테스트 8 〉	통과 (1.25ms, 10.7MB)
테스트 9 〉	통과 (0.77ms, 10.8MB)
테스트 10 〉	통과 (1.06ms, 10.7MB)
테스트 11 〉	통과 (0.37ms, 10.6MB)
테스트 12 〉	통과 (0.37ms, 10.4MB)
테스트 13 〉	통과 (0.71ms, 10.7MB)
테스트 14 〉	통과 (1.34ms, 10.7MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.4MB)
테스트 18 〉	통과 (0.09ms, 10.4MB)
테스트 19 〉	통과 (0.74ms, 10.8MB)
테스트 20 〉	통과 (0.66ms, 10.5MB)
테스트 21 〉	통과 (1.05ms, 10.6MB)
테스트 22 〉	통과 (0.77ms, 10.5MB)
테스트 23 〉	통과 (0.74ms, 10.7MB)
테스트 24 〉	통과 (1.32ms, 10.8MB)
테스트 25 〉	통과 (124.07ms, 56.7MB)
테스트 26 〉	통과 (127.31ms, 61.1MB)
테스트 27 〉	통과 (111.90ms, 64.6MB)
테스트 28 〉	통과 (126.35ms, 65.5MB)
테스트 29 〉	통과 (119.04ms, 65.3MB)
테스트 30 〉	통과 (103.67ms, 58.9MB)
테스트 31 〉	통과 (91.21ms, 62MB)
테스트 32 〉	통과 (84.22ms, 57.3MB)
"""


def solution(record):
    nickname_id = {}

    logs = []
    for log in record:
        tmp = log.split(' ')
        logs.append((tmp[0], tmp[1]))
        if len(tmp) > 2:
            nickname_id[tmp[1]] = tmp[2]

    answer = []
    for log in logs:
        if log[0] == 'Enter':
            answer.append(f'{nickname_id[log[1]]}님이 들어왔습니다.')
        elif log[0] == 'Leave':
            answer.append(f'{nickname_id[log[1]]}님이 나갔습니다.')
        else:  # Change
            pass
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi",
              "Enter uid4567 Prodo",
              "Leave uid1234",
              "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]


    print(solution(record))