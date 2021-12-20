"""
https://programmers.co.kr/learn/courses/30/lessons/17683

테스트 1 〉	통과 (2.30ms, 10.9MB)
테스트 2 〉	통과 (3.17ms, 10.9MB)
테스트 3 〉	통과 (3.53ms, 10.9MB)
테스트 4 〉	통과 (2.35ms, 10.9MB)
테스트 5 〉	통과 (2.22ms, 10.9MB)
테스트 6 〉	통과 (3.17ms, 10.8MB)
테스트 7 〉	통과 (3.36ms, 10.8MB)
테스트 8 〉	통과 (3.78ms, 10.9MB)
테스트 9 〉	통과 (2.37ms, 10.8MB)
테스트 10 〉	통과 (2.42ms, 10.9MB)
테스트 11 〉	통과 (3.38ms, 11MB)
테스트 12 〉	통과 (3.03ms, 10.9MB)
테스트 13 〉	통과 (2.54ms, 10.9MB)
테스트 14 〉	통과 (2.61ms, 10.9MB)
테스트 15 〉	통과 (2.90ms, 10.9MB)
테스트 16 〉	통과 (2.40ms, 10.8MB)
테스트 17 〉	통과 (3.26ms, 10.9MB)
테스트 18 〉	통과 (3.95ms, 10.9MB)
테스트 19 〉	통과 (2.55ms, 10.8MB)
테스트 20 〉	통과 (2.60ms, 10.8MB)
테스트 21 〉	통과 (3.71ms, 10.8MB)
테스트 22 〉	통과 (3.85ms, 10.9MB)
테스트 23 〉	통과 (3.39ms, 10.8MB)
테스트 24 〉	통과 (3.22ms, 10.8MB)
테스트 25 〉	통과 (2.36ms, 10.9MB)
테스트 26 〉	통과 (2.99ms, 10.9MB)
테스트 27 〉	통과 (3.20ms, 10.9MB)
테스트 28 〉	통과 (2.20ms, 10.8MB)
테스트 29 〉	통과 (3.97ms, 10.9MB)
테스트 30 〉	통과 (3.68ms, 10.9MB)
"""
from datetime import datetime


def solution(m, musicinfos):
    ans = ''
    mx = - 1
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].split(',')

        # 분 간격을 구한다
        time_1 = datetime.strptime(musicinfo[0], "%H:%M")
        time_2 = datetime.strptime(musicinfo[1], "%H:%M")
        minutes = (time_2 - time_1).seconds // 60

        # 중복되는 음을 독립되게 한다. (C#의 경우 이미 C가 존재하므로, 중복됨)
        alter = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}
        for k in alter.keys():
            m = m.replace(k, alter[k])
            musicinfo[3] =  musicinfo[3].replace(k, alter[k])

        # 곡별 멜로디를 구한다.
        plays, one_more = divmod(minutes, len(musicinfo[3]))
        melody = musicinfo[3] * plays + musicinfo[3][:one_more]

        # m과 매칭되는 음악 제목을 찾는다.
        if m in melody:
            # 재생된 시간을 비교하고. 이미 매칭된 음악보다 길이가 길면 갱신한다. (같으면 X)
            if minutes > mx:
                mx = minutes
                ans = musicinfo[2]

    if ans == '':
        return "(None)"
    return ans

if __name__ == '__main__':
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    m = 'ABCDEFG'

    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    m = "CC#BCC#BCC#BCC#B"

    musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    m = 'ABC'

    # 사용된 음
    # "C, C#, D, D#, E, F, F#, G, G#, A, A#, B"

    print(solution(m, musicinfos))