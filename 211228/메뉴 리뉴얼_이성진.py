# https://programmers.co.kr/learn/courses/30/lessons/72411
"""

테스트 1 〉	통과 (0.11ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.11ms, 10.4MB)
테스트 6 〉	통과 (0.26ms, 10.2MB)
테스트 7 〉	통과 (0.28ms, 10.3MB)
테스트 8 〉	통과 (2.83ms, 10.3MB)
테스트 9 〉	통과 (2.09ms, 10.3MB)
테스트 10 〉	통과 (4.58ms, 10.7MB)
테스트 11 〉	통과 (1.81ms, 10.3MB)
테스트 12 〉	통과 (2.24ms, 10.3MB)
테스트 13 〉	통과 (3.13ms, 10.6MB)
테스트 14 〉	통과 (2.32ms, 10.5MB)
테스트 15 〉	통과 (3.28ms, 10.5MB)
테스트 16 〉	통과 (0.94ms, 10.3MB)
테스트 17 〉	통과 (0.43ms, 10.3MB)
테스트 18 〉	통과 (0.21ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (0.87ms, 10.2MB)
"""


from itertools import combinations


def solution(orders, courses):
    tmp = []

    # course에 적힌 갯수 조합으로 뽑은 후 딕셔너리 담기
    for course in courses:
        menu = dict()
        for order in orders:
            for t in combinations(order, course):
                t = ''.join(sorted(t))

                menu[t] = menu.get(t, 0) + 1

        # value 기준으로 내림차순 정렬 수행하고, 가장 앞에 있는 key의 값과 같은 녀석들 tmp로 담기
        menu = sorted(menu.items(), key=lambda x: (-x[1], x[0]))
        if menu and menu[0][1] > 1:
            mx = menu[0][1]
            tmp.append(menu[0][0])

            for i in range(1, len(menu)):
                if menu[i][1] < mx:
                    break
                tmp.append(menu[i][0])

    return sorted(tmp)


if __name__ == '__main__':
    # ["AC", "ACDE", "BCFG", "CDE"]
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]

    # # ["ACD", "AD", "ADE", "CD", "XYZ"]
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]
    #
    # # ['WX', 'XY']
    orders = ["XYZ", "XWY", "WXA"]
    course = [2, 3, 4]

    print(solution(orders, course))