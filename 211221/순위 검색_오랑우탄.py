"""
https://programmers.co.kr/learn/courses/30/lessons/72412

테스트 1 〉	통과 (0.31ms, 10.5MB)
테스트 2 〉	통과 (0.19ms, 10.5MB)
테스트 3 〉	통과 (0.28ms, 10.4MB)
테스트 4 〉	통과 (2.23ms, 10.5MB)
테스트 5 〉	통과 (2.35ms, 10.6MB)
테스트 6 〉	통과 (4.18ms, 10.6MB)
테스트 7 〉	통과 (2.50ms, 10.8MB)
테스트 8 〉	통과 (37.16ms, 11.4MB)
테스트 9 〉	통과 (41.06ms, 13.2MB)
테스트 10 〉	통과 (61.95ms, 13.9MB)
테스트 11 〉	통과 (2.13ms, 10.6MB)
테스트 12 〉	통과 (6.19ms, 10.7MB)
테스트 13 〉	통과 (2.53ms, 10.7MB)
테스트 14 〉	통과 (19.90ms, 12.3MB)
테스트 15 〉	통과 (20.63ms, 12.2MB)
테스트 16 〉	통과 (1.87ms, 10.6MB)
테스트 17 〉	통과 (4.73ms, 10.7MB)
테스트 18 〉	통과 (19.76ms, 12.1MB)
효율성  테스트
테스트 1 〉	통과 (771.51ms, 63.8MB)
테스트 2 〉	통과 (781.62ms, 64.1MB)
테스트 3 〉	통과 (800.79ms, 63.5MB)
테스트 4 〉	통과 (816.75ms, 64MB)
"""
from collections import defaultdict


def solution(info, query):
    data = defaultdict(list)

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        # ['python', 'and', 'frontend', 'and', 'senior', 'and', 'chicken', '200']
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)

    return answer


if __name__ == '__main__':
    # [1, 1, 1, 1, 2, 4]
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]

    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]
    print(solution(info, query))
