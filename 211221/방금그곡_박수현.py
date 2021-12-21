"""
https://programmers.co.kr/learn/courses/30/lessons/17683

정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.6MB)
테스트 3 〉	통과 (0.03ms, 10.6MB)
테스트 4 〉	통과 (0.03ms, 10.5MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.09ms, 10.6MB)
테스트 8 〉	통과 (0.07ms, 10.5MB)
테스트 9 〉	통과 (0.09ms, 10.4MB)
테스트 10 〉	통과 (0.07ms, 10.4MB)
테스트 11 〉	통과 (0.06ms, 10.5MB)
테스트 12 〉	통과 (0.07ms, 10.5MB)
테스트 13 〉	통과 (0.07ms, 10.5MB)
테스트 14 〉	통과 (0.11ms, 10.4MB)
테스트 15 〉	통과 (0.11ms, 10.5MB)
테스트 16 〉	통과 (0.07ms, 10.5MB)
테스트 17 〉	통과 (0.10ms, 10.5MB)
테스트 18 〉	통과 (0.06ms, 10.5MB)
테스트 19 〉	통과 (0.12ms, 10.4MB)
테스트 20 〉	통과 (0.10ms, 10.5MB)
테스트 21 〉	통과 (0.10ms, 10.4MB)
테스트 22 〉	통과 (0.09ms, 10.5MB)
테스트 23 〉	통과 (0.07ms, 10.5MB)
테스트 24 〉	통과 (0.10ms, 10.5MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.04ms, 10.5MB)
테스트 27 〉	통과 (0.03ms, 10.4MB)
테스트 28 〉	통과 (0.03ms, 10.5MB)
테스트 29 〉	통과 (4.51ms, 12.4MB)
테스트 30 〉	통과 (4.74ms, 13.3MB)

조건
- 네오가 찾으려는 음악을 구하라
1. ["시작 시간","끝나는 시간","노래 제목","악보"]
2. 음악 길이 < 재생된 시간: 처음부터 반복 재생(음악 끝과 처음이 이어질 수 있음)
3. 조건 일치가 여러개인 경우, 재생 시간이 제일 긴, 먼저 입력된 제목 리턴
4. 조건 일치하지 않는 경우 None 리턴

알고리즘
~문자열 처리
1. 끝 시간 - 시작 시간 = 총 시간 구하기
2. 악보 중 #들어간 문자 소문자로 치환
3. 총 시간에 따른 최종 멜로디 구하
4. 사용자가 들은 음원이 멜로디에 있다면 더 긴 시간을 가진 제목을 저장
"""
def change_melody(s):
    s = s.replace('A#', 'a')
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    return s

def get_time(start, end):
    start = list(map(int, start.split(":")))
    end = list(map(int, end.split(":")))
    hour = end[0] - start[0]
    minute = end[1] - start[1]
    return hour * 60 + minute

def solution(m, musicinfos):
    answer = ('(None)', None)
    m = change_melody(m)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        # 1: 총 시간 구하기
        time = get_time(start, end)
        # 2: #붙은 문자 소문자로 치환
        melody = change_melody(melody)
        # 3: 총 시간에 따른 최종 멜로디 구함
        melody = (melody * time)[:time]
        # 4: 사용자가 들은 음원이 멜로디에 있다면 더 긴 시간을 가진 제목을 저장
        if m in melody:
            if answer[1] == None or answer[1] < time:
                answer = (title, time)
    return answer[0]
