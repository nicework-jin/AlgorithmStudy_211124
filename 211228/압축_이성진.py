# https://programmers.co.kr/learn/courses/30/lessons/17684
"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.17ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.29ms, 10.4MB)
테스트 7 〉	통과 (0.25ms, 10.2MB)
테스트 8 〉	통과 (0.30ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.50ms, 10.2MB)
테스트 11 〉	통과 (0.18ms, 10.3MB)
테스트 12 〉	통과 (0.30ms, 10.3MB)
테스트 13 〉	통과 (0.40ms, 10.3MB)
테스트 14 〉	통과 (0.41ms, 10.2MB)
테스트 15 〉	통과 (0.38ms, 10.3MB)
테스트 16 〉	통과 (0.30ms, 10.2MB)
테스트 17 〉	통과 (0.30ms, 10.3MB)
테스트 18 〉	통과 (0.16ms, 10.2MB)
테스트 19 〉	통과 (0.12ms, 10.3MB)
테스트 20 〉	통과 (0.26ms, 10.3MB)
"""


def solution(msg):
    book = {}
    answer= []
    for i in range(26):
        book[chr(65+i)] = i + 1

    curr = 0
    next = 0
    while True:
        next += 1
        if next == len(msg):
            answer.append(book[msg[curr:next]])
            break

        if msg[curr:next+1] not in book:
            book[msg[curr:next+1]] = len(book) + 1
            answer.append(book[msg[curr:next]])
            curr = next

    return answer



    return


if __name__ == '__main__':
    # [11, 1, 27, 15]
    msg = 'KAKAO'

    solution(msg)