'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (1.34ms, 10.4MB)
테스트 5 〉	통과 (41.74ms, 10.3MB)
테스트 6 〉	통과 (4.80ms, 10.3MB)
테스트 7 〉	통과 (0.61ms, 10.4MB)
테스트 8 〉	통과 (1.31ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.65ms, 10.3MB)
테스트 11 〉	통과 (1.50ms, 10.4MB)
'''
def solution(m, n, board):
    box = [(0, 1), (1, 0), (1, 1)]
    
    graph = []
    answer = 0
    
    for row in board:
        graph.append(list(row))
        
    while True:
        rm_set = set()
        for y in range(m-1):
            for x in range(n-1):
                if graph[y][x] == 'X':
                    continue

                init_val = graph[y][x]

                for dy, dx in box:
                    ny = y + dy
                    nx = x + dx

                    if init_val != graph[ny][nx]:
                        break
                else:
                    rm_set.add(tuple([y, x]))
                    for dy, dx in box:
                        ny = y + dy
                        nx = x + dx
                        rm_set.add(tuple([ny, nx]))
        if not rm_set:
            break
        else:
            answer += len(rm_set)

        for ry, rx in rm_set:
            graph[ry][rx] = 'X'

        for x in range(len(graph[0])):
            for y in range(len(graph) -1, -1, -1):
                if graph[y][x] == 'X':
                    for gy in range(y-1, -1, -1):
                        if graph[gy][x] != 'X':
                            graph[y][x] = graph[gy][x]
                            graph[gy][x] = 'X'
                            break
                    else:
                        break
    
    return answer

# from collections import deque

# def solution(m, n, board):
#     board = deque(map(list, zip(*reversed(board))))
    
#     def game_start(prev_cnt, re_board):
#         rm_lst = []
#         cnt = 0
        
#         for i in range(1, n):
#             for j in range(1, m):
                
#                 if re_board[i][j] == '@':
#                     continue
                    
#                 if re_board[i][j] == re_board[i - 1][j] == re_board[i][j - 1] == re_board[i - 1][j - 1]:
#                     rm_lst.append([i, j])
#                     rm_lst.append([i - 1, j])
#                     rm_lst.append([i, j - 1])
#                     rm_lst.append([i - 1, j - 1])

#         for i, j in rm_lst:
#             re_board[i][j] = '@'

#         for i, row in enumerate(re_board):
#             tmp_row = deque([])

#             while row:
#                 if row[-1] != '@':
#                     tmp_row.appendleft(row.pop())
#                 else:
#                     cnt += 1
#                     row.pop()
#                     tmp_row.append('@')
#             else:
#                 re_board[i] = tmp_row
        
#         return cnt if cnt == prev_cnt else game_start(cnt, re_board)
        
#     return game_start(0, board)