"""
https://programmers.co.kr/learn/courses/30/lessons/42885


테스트 1 〉	통과 (0.79ms, 10.2MB)
테스트 2 〉	통과 (0.62ms, 10.2MB)
테스트 3 〉	통과 (0.55ms, 10.3MB)
테스트 4 〉	통과 (0.53ms, 10.2MB)
테스트 5 〉	통과 (0.30ms, 10.2MB)
테스트 6 〉	통과 (0.18ms, 10.2MB)
테스트 7 〉	통과 (0.30ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.56ms, 10.3MB)
테스트 11 〉	통과 (0.47ms, 10.3MB)
테스트 12 〉	통과 (0.46ms, 10.3MB)
테스트 13 〉	통과 (0.69ms, 10.3MB)
테스트 14 〉	통과 (0.75ms, 10.3MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (8.60ms, 10.6MB)
테스트 2 〉	통과 (9.56ms, 10.6MB)
테스트 3 〉	통과 (7.49ms, 10.4MB)
테스트 4 〉	통과 (9.39ms, 10.6MB)
테스트 5 〉	통과 (7.74ms, 10.5MB)
"""


def solution(people, limit):
    lenght = len(people)
    people.sort(reverse=True)

    x = 0
    # boat_num = [0] * lenght

    start = 0
    end = lenght-1
    while start <= end:
        x += 1
        if people[start] + people[end] <= limit:
            # boat_num[end] = x
            end -= 1
        # boat_num[start] = x
        start += 1

    return x


if __name__ == '__main__':
    # 3
    people = [70, 50, 80, 50]
    limit = 100

    # 3
    people = [10, 20, 30, 50]
    limit = 50

    # people = [50, 50, 50, 10]
    # limit = 50
    print(solution(people, limit))
