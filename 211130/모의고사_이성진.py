"""
https://programmers.co.kr/learn/courses/30/lessons/42840

테스트 1 〉	통과 (0.20ms, 10.5MB)
테스트 2 〉	통과 (0.28ms, 10.6MB)
테스트 3 〉	통과 (0.26ms, 10.5MB)
테스트 4 〉	통과 (0.32ms, 10.5MB)
테스트 5 〉	통과 (0.21ms, 10.5MB)
테스트 6 〉	통과 (0.22ms, 10.5MB)
테스트 7 〉	통과 (2.02ms, 10.4MB)
테스트 8 〉	통과 (0.78ms, 10.5MB)
테스트 9 〉	통과 (6.08ms, 10.5MB)
테스트 10 〉	통과 (1.67ms, 10.5MB)
테스트 11 〉	통과 (6.09ms, 10.5MB)
테스트 12 〉	통과 (3.07ms, 10.6MB)
테스트 13 〉	통과 (0.62ms, 10.6MB)
테스트 14 〉	통과 (6.80ms, 10.5MB)
"""


def solution(answers):
    submitions = {
        # 수포자번호: [답지]
        '1': [1, 2, 3, 4, 5] * 2000,
        '2': [2, 1, 2, 3, 2, 4, 2, 5] * 1250,
        '3': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    }
    cnt = {'1': 0, '2': 0, '3': 0}

    for i in range(len(answers)):
        for supoja in submitions.keys():
            if submitions[supoja][i] == answers[i]:
                cnt[supoja] += 1

    mx = max(cnt.values())
    return [int(k) for k, v in cnt.items() if v == mx]


if __name__ == "__main__":
    # [1]
    answers = [1, 2, 3, 4, 5]

    # [1, 2, 3]
    # answers = [1,3,2,4,2]

    print(solution(answers))