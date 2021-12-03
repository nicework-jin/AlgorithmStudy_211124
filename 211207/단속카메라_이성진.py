"""
https://programmers.co.kr/learn/courses/30/lessons/42884

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.41ms, 10.4MB)
테스트 2 〉	통과 (0.44ms, 10.3MB)
테스트 3 〉	통과 (0.85ms, 10.5MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.91ms, 10.6MB)

풀이: https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
- 정렬
- 최초로 범위에 포함되지 않는 녀석의 개수..
"""


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    camera = -30001

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


if __name__ == '__main__':
    # 2
    routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

    # 1
    routes = [[0, 2], [1, 3], [2, 4], [2, 5]]

    # 2
    routes = [[0, 2], [1, 3], [2, 4], [3, 5]]
    print(solution(routes))

