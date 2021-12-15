# https://programmers.co.kr/learn/courses/30/lessons/60058
"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.4MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.3MB)
테스트 15 〉	통과 (0.10ms, 10.3MB)
테스트 16 〉	통과 (0.37ms, 10.3MB)
테스트 17 〉	통과 (0.20ms, 10.4MB)
테스트 18 〉	통과 (0.28ms, 10.2MB)
테스트 19 〉	통과 (0.41ms, 10.3MB)
테스트 20 〉	통과 (0.35ms, 10.3MB)
테스트 21 〉	통과 (0.34ms, 10.3MB)
테스트 22 〉	통과 (0.18ms, 10.3MB)
테스트 23 〉	통과 (0.28ms, 10.3MB)
테스트 24 〉	통과 (0.14ms, 10.3MB)
테스트 25 〉	통과 (0.20ms, 10.4MB)
"""


def validate(w):
    w = list(w)[::-1]
    stack = []
    while w:
        tmp = w.pop()
        if stack:
            if stack[-1] == '(' and tmp == ')':
                stack.pop()
            else:
                stack.append(tmp)
        else:
            stack.append(tmp)
    if stack:
        return False
    else:
        return True


def solution(w):
    if w == '':
        return ''

    o = 0
    c = 0
    u = ''
    v = ''
    for i in range(len(w)):
        if w[i] == '(':
            o += 1
        else:
            c += 1

        if o == c:
            u = w[:i+1]
            v = w[i+1:]
            break

    if validate(u):
        return u + solution(v)
    else:
        u = u[1:-1]
        tmp = ''
        for i in range(len(u)):
            if u[i] == ')':
                tmp += '('
            else:
                tmp += ')'
        return '(' + solution(v) + ')' + tmp


if __name__ == '__main__':

    # "(()())()"
    p = "(()())()"

    # # "()"
    # p = ")("

    # "()(())()"
    # p = "() ))((()"

    print(solution(p))
    # print(validate(p))