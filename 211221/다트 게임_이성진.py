# https://programmers.co.kr/learn/courses/30/lessons/17682

"""
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.5MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.4MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)
테스트 20 〉	통과 (0.02ms, 10.3MB)
테스트 21 〉	통과 (0.02ms, 10.3MB)
테스트 22 〉	통과 (0.02ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.02ms, 10.2MB)
테스트 27 〉	통과 (0.03ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
테스트 30 〉	통과 (0.02ms, 10.4MB)
테스트 31 〉	통과 (0.02ms, 10.4MB)
테스트 32 〉	통과 (0.02ms, 10.4MB)
"""
def solution(dartResult):
    dartResult = dartResult.replace('10', 'X')

    scores = []
    for r in dartResult:
        if r.isdigit() or r == 'X':
            if r == 'X':
                r = 10
            scores.append(int(r))

        elif r == 'S':
            scores[-1] = scores[-1] ** 1

        elif r == 'D':
            scores[-1] = scores[-1] ** 2

        elif r == 'T':
            scores[-1] = scores[-1] ** 3

        elif r == '*':
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2

        else:  # r=='#'
            scores[-1] *= -1

    return sum(scores)


if __name__ == '__main__':
    # 37
    dartResult = '1S2D*3T'

    # # 9
    dartResult = '1D2S#10S'

    # # 3
    dartResult = '1D2S0T'
    #
    # # 23
    dartResult = '1S*2T*3S'
    #
    # # 5
    dartResult = '1D#2S*3S'
    #
    # # -4
    dartResult = '1T2D3D#'
    #
    # # 59
    dartResult = '1D2S3T*'

    print(solution(dartResult))