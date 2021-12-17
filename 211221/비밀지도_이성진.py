"""
https://programmers.co.kr/learn/courses/30/lessons/17681

테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
"""


def solution(n, arr1, arr2):
    """
    '|' 로 비트 연산
    ex) 0b101110 | 0b11011이면, 0b111111 출력
    앞에 붙은 0b는 2진수를 나타내는 표현
    """

    answer = []

    for i in range(len(arr1)):
        merged_map = bin(arr1[i] | arr2[i])[2:]

        while len(merged_map) < n:
            merged_map = '0' + merged_map

        merged_map = merged_map.replace('1', '#')
        merged_map = merged_map.replace('0', ' ')
        answer.append(merged_map)

    return answer


if __name__ == '__main__':
    # ["#####", "# # #", "### #", "# ##", "#####"]
    n =	5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    # ["######", "### #", "## ##", " #### ", " #####", "### # "]
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]

    print(solution(n, arr1, arr2))
