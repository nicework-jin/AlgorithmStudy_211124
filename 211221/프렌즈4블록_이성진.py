# https://programmers.co.kr/learn/courses/30/lessons/17679
"""
테스트 1 〉	통과 (0.14ms, 10.5MB)
테스트 2 〉	통과 (0.11ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (1.29ms, 10.3MB)
테스트 5 〉	통과 (189.38ms, 10.4MB)
테스트 6 〉	통과 (15.81ms, 10.4MB)
테스트 7 〉	통과 (1.37ms, 10.4MB)
테스트 8 〉	통과 (1.37ms, 10.4MB)
테스트 9 〉	통과 (0.14ms, 10.5MB)
테스트 10 〉	통과 (0.86ms, 10.4MB)
테스트 11 〉	통과 (2.42ms, 10.4MB)
"""

from copy import deepcopy


def solution(m, n, board):
    # zip 함수를 이용해서 가로/세로 방향을 바꾼다. >> m과 n의 역할이 서로 바뀜
    board = list(map(list, zip(*board)))
    res = 0

    def game(board):
        res = 0
        copy_board = deepcopy(board)

        for x in range(m - 1):
            for y in range(n - 1):
                if board[y][x] == 'X':
                    continue

                if board[y][x] == board[y][x + 1] == board[y + 1][x] == board[y + 1][x + 1]:
                    copy_board[y][x] = '_'
                    copy_board[y][x + 1] = '_'
                    copy_board[y + 1][x] = '_'
                    copy_board[y + 1][x + 1] = '_'

        # 터지지 않은 블록을 안 쪽으로 몰아 넣는다.
        for i, v in enumerate(copy_board):
            cnt = v.count('_')
            res += cnt
            board[i] = ['X'] * cnt + [a for a in v if a != '_']
        return res, board

    while True:
        cnt, board = game(board)
        if cnt == 0:
            return res
        res += cnt


if __name__ == '__main__':
    # 14
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

    # 15
    # m = 6
    # n = 6
    # board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

    # m = 3
    # n = 3
    # board = ["TTT",
    #          "TTF",
    #          "FFF"]
    print(solution(m, n, board))