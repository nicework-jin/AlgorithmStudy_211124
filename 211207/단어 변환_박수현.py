"""
https://programmers.co.kr/learn/courses/30/lessons/43163

조건
- begin에서 target으로 변환하는 가장 짧은 과정을 찾기
1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
2. words에 있는 단어로만 변환 가능
3. words에 중복되는 단어 없음
4. 변환할 수 없는 경우 0 리턴

알고리즘
1. 방문한 노드는 집합으로 생성
2. 현 단어가 target과 같다면 cnt 리턴
3. 현 단어와 바꿀 수 있는 단어인지 검사(1개 차이)
4. 바꿀 수 있다면 큐에 넣고 방문
"""
from collections import deque


def can_change(cur_word, words):
    can_list = []
    for word in words:
        diff = []
        for x, y in zip(cur_word, word):
            if x != y:
                diff.append(False)
        if len(diff) == 1:
            can_list.append(word)
    return can_list


def solution(begin, target, words):
    # 1
    visited = set([begin])
    q = deque([(begin, 0)])

    while q:
        cur_word, cur_cnt = q.popleft()
        # 2
        if cur_word == target:
            return cur_cnt
        # 3
        for word in can_change(cur_word, words):
            if word not in visited:
                # 4
                q.append((word, cur_cnt + 1))
                visited.add(word)
    return 0
