"""
https://programmers.co.kr/learn/courses/30/lessons/72412
테스트 1 〉	통과 (0.20ms, 10.4MB)
테스트 2 〉	통과 (0.20ms, 10.4MB)
테스트 3 〉	통과 (0.29ms, 10.5MB)
테스트 4 〉	통과 (1.17ms, 10.5MB)
테스트 5 〉	통과 (2.01ms, 10.5MB)
테스트 6 〉	통과 (5.00ms, 10.5MB)
테스트 7 〉	통과 (2.59ms, 10.8MB)
테스트 8 〉	통과 (42.09ms, 11.5MB)
테스트 9 〉	통과 (38.81ms, 13.3MB)
테스트 10 〉	통과 (39.81ms, 13.8MB)
테스트 11 〉	통과 (1.94ms, 10.6MB)
테스트 12 〉	통과 (4.45ms, 10.7MB)
테스트 13 〉	통과 (2.53ms, 10.7MB)
테스트 14 〉	통과 (19.71ms, 12MB)
테스트 15 〉	통과 (20.08ms, 11.9MB)
테스트 16 〉	통과 (1.85ms, 10.7MB)
테스트 17 〉	통과 (4.41ms, 10.7MB)
테스트 18 〉	통과 (23.69ms, 12.1MB)
효율성  테스트
테스트 1 〉	통과 (795.87ms, 63.8MB)
테스트 2 〉	통과 (769.03ms, 63.5MB)
테스트 3 〉	통과 (767.08ms, 63.2MB)
테스트 4 〉	통과 (767.16ms, 64.2MB)

다른 사람 풀이인데, 깔끔해서 올렸어요
잔재주 안 부리고 직관적으로 풀어서 좋더라구요.

딕셔너리 정의할 때도 collections.defaultdict 라이브러리 안쓰고, dict로 하네요.
안 쓰는 key도 미리 정의해놔서 느릴 줄 알았는데, 오히려 빨라요
"""


def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        # [java, backend, junior, pizza, 150]
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
