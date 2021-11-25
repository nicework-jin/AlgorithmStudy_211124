"""
https://programmers.co.kr/learn/courses/30/lessons/42579

정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.4MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.11ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.10ms, 10.2MB)
테스트 14 〉	통과 (0.12ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)

조건
- 가장 많이 재생된 노래 두 개씩 출시
1. 속한 노래가 가장 많이 재생된 장르
2. 장르 내에서 많이 재생된 노래
2-1. 장르 내에서 재생 횟수 같으면 고유번호 낮은 순서대로

알고리즘
1. for genre, play in zip(genres, plays):
1-1. {genre_cnt: "genre": int(n)} 총 플레이 횟수 저장
1-2. {genre_play: "genre": [play, play...]} 장르별 플레이 횟수 배열 저장
2. genre_cnt의 value 값을(총 플레이 횟수) 역순으로 정렬
3. genre_cnt 모든 원소 탐색
4. genre_play[genre]의 배열을 정렬하고 2개까지 정답에 저장
"""
from collections import defaultdict
from operator import itemgetter


def solution(genres, plays):
    answer = []
    genre_cnt = defaultdict(int)
    genre_play = defaultdict(list)
    # 1
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # 1-1
        genre_cnt[genre] += play
        # 1-2
        genre_play[genre].append([int(play), int(idx)])
    # 2
    genre_cnt = sorted(genre_cnt.items(), key=itemgetter(1), reverse=True)
    # 3
    for genre, _ in genre_cnt:
        # 4
        for play, idx in sorted(genre_play[genre], key=lambda x: x[0], reverse=True)[:2]:
            answer.append(idx)
    return answer
