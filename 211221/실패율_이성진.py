# https://programmers.co.kr/learn/courses/30/lessons/42889
"""
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (2.13ms, 10.6MB)
테스트 4 〉	통과 (6.76ms, 10.9MB)
테스트 5 〉	통과 (27.40ms, 15MB)
테스트 6 〉	통과 (0.13ms, 10.3MB)
테스트 7 〉	통과 (0.66ms, 10.3MB)
테스트 8 〉	통과 (6.41ms, 10.9MB)
테스트 9 〉	통과 (18.19ms, 15.1MB)
테스트 10 〉	통과 (6.74ms, 10.9MB)
테스트 11 〉	통과 (6.66ms, 10.9MB)
테스트 12 〉	통과 (9.99ms, 11.4MB)
테스트 13 〉	통과 (11.30ms, 11.5MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (4.41ms, 10.6MB)
테스트 16 〉	통과 (2.19ms, 10.4MB)
테스트 17 〉	통과 (4.35ms, 10.7MB)
테스트 18 〉	통과 (2.25ms, 10.4MB)
테스트 19 〉	통과 (0.47ms, 10.3MB)
테스트 20 〉	통과 (4.68ms, 10.4MB)
테스트 21 〉	통과 (7.46ms, 10.8MB)
테스트 22 〉	통과 (26.43ms, 18.4MB)
테스트 23 〉	통과 (13.68ms, 11.7MB)
테스트 24 〉	통과 (13.53ms, 11.7MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
"""


def solution(N, stages):
    cnt = dict()
    for i in range(0, N+2):
        cnt.setdefault(i, int())

    for stage in stages:
        cnt[stage] += 1

    ans = []
    ratio = [0] * (N+1)
    bunmo = len(stages)
    for i in range(N):
        if (bunmo := (bunmo - cnt[i])) <= 0:
            bunmo = 1
        ans.append((cnt[i+1] / bunmo, i+1))

    return list(map(lambda x: x[1], sorted(ans, key=lambda x: (-x[0], x[1]))))


if __name__ == '__main__':
    #  [3, 4, 2, 1, 5]  # 실패율이 높은 스테이지부터! 내림차순!
    N = 5  # 전체 스테이지 수
    stages = [2, 1, 2, 6, 2, 4, 3, 3]

    N = 4
    stages = [4, 4, 4, 4, 4]

    N = 1
    stages = [1, 1, 1, 1, 1]

    N = 4
    stages= [1,2,3,2,1]
    print(solution(N, stages))