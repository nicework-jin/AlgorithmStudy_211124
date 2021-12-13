"""
테스트 1 〉	통과 (0.12ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (0.20ms, 10.2MB)
테스트 4 〉	통과 (0.21ms, 10.3MB)
테스트 5 〉	통과 (0.13ms, 10.4MB)
테스트 6 〉	통과 (0.48ms, 10.3MB)
테스트 7 〉	통과 (0.80ms, 10.2MB)
테스트 8 〉	통과 (4.19ms, 10.3MB)
테스트 9 〉	통과 (2.71ms, 10.3MB)
테스트 10 〉	통과 (4.15ms, 10.5MB)
테스트 11 〉	통과 (2.00ms, 10.3MB)
테스트 12 〉	통과 (2.48ms, 10.3MB)
테스트 13 〉	통과 (3.42ms, 10.4MB)
테스트 14 〉	통과 (2.42ms, 10.4MB)
테스트 15 〉	통과 (3.72ms, 10.4MB)
테스트 16 〉	통과 (1.01ms, 10.3MB)
테스트 17 〉	통과 (0.49ms, 10.3MB)
테스트 18 〉	통과 (0.19ms, 10.3MB)
테스트 19 〉	통과 (0.04ms, 10.2MB)
테스트 20 〉	통과 (1.29ms, 10.3MB)
"""

from itertools import combinations


def solution(orders, course):
    answer = []
    for n in course:
        cnt = {}
        for order in orders:
            tmp_list = list(map(lambda x: ''.join(x), combinations(order, n)))

            # n개로 구성된 메뉴 조합 (all)
            for tmp in tmp_list:
                x = ''.join(sorted(tmp))
                cnt[x] = cnt.get(x, 0) + 1

            # 조건에 맞는 메뉴 조합만 선출
            mx = -1
            tmp = []
            for menu, num in cnt.items():
                if num < 2:
                    continue

                if mx > num:
                    continue

                if mx < num:
                    tmp = [menu]
                    mx = num

                if mx == num and menu not in tmp:
                    tmp.append(menu)
        answer.extend(sorted(tmp))
    return sorted(answer)







if __name__ == '__main__':
    # ["AC", "ACDE", "BCFG", "CDE"]
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]

    # ["ACD", "AD", "ADE", "CD", "XYZ"]
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]

    # ['WX', 'XY']
    # orders = ["XYZ", "XWY", "WXA"]
    # course = [2, 3, 4]

    print(solution(orders, course))