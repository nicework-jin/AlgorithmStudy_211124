"""
https://programmers.co.kr/learn/courses/30/lessons/72414
정확성  테스트
테스트 1 〉	통과 (1.43ms, 10.5MB)
테스트 2 〉	통과 (6.87ms, 10.6MB)
테스트 3 〉	통과 (15.36ms, 11.3MB)
테스트 4 〉	통과 (183.25ms, 28MB)
테스트 5 〉	통과 (261.27ms, 34.3MB)
테스트 6 〉	통과 (127.97ms, 21.6MB)
테스트 7 〉	통과 (405.79ms, 41.1MB)
테스트 8 〉	통과 (393.22ms, 45.9MB)
테스트 9 〉	통과 (545.13ms, 54.4MB)
테스트 10 〉	통과 (573.66ms, 54.7MB)
테스트 11 〉	통과 (581.96ms, 52.1MB)
테스트 12 〉	통과 (527.18ms, 49.7MB)
테스트 13 〉	통과 (598.57ms, 54.6MB)
테스트 14 〉	통과 (425.98ms, 40.8MB)
테스트 15 〉	통과 (44.80ms, 15.2MB)
테스트 16 〉	통과 (418.51ms, 40.8MB)
테스트 17 〉	통과 (602.23ms, 54.8MB)
테스트 18 〉	통과 (578.51ms, 42.2MB)
테스트 19 〉	통과 (1.50ms, 10.5MB)
테스트 20 〉	통과 (1.75ms, 10.5MB)
테스트 21 〉	통과 (125.95ms, 20.3MB)
테스트 22 〉	통과 (124.55ms, 20.2MB)
테스트 23 〉	통과 (504.83ms, 47.1MB)
테스트 24 〉	통과 (448.58ms, 40.8MB)
테스트 25 〉	통과 (96.35ms, 19.7MB)
테스트 26 〉	통과 (60.51ms, 15MB)
테스트 27 〉	통과 (69.99ms, 17.6MB)
테스트 28 〉	통과 (62.89ms, 17MB)
테스트 29 〉	통과 (64.29ms, 16.9MB)
테스트 30 〉	통과 (42.89ms, 14.2MB)
테스트 31 〉	통과 (50.06ms, 14.9MB)

조건
- 시청자들의 누적 재생시간이 가장 많이 나오는 시작 시각을 구해서 리턴하라. 만약 여러 곳이라면, 그 중에서 가장 빠른 시작 시각을 리턴

알고리즘
1. 시간을 초단위로 바꿔서 배열로 저장
2. log내의 모든 시간에 대해 start, end 값에 1, -1씩 증가
3. 구간별로 start와 end 사이 사람 수를 채움
4. 전체 범위에서 [i] = [i] + [i-1]로 누적 사람 수를 채움
5. 가장 사람이 많은 구간을 구함
6. 5번의 int를 문자열로 바꿔서 리턴
"""

def str_to_int(time):
    h,m,s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h+':'+m+':'+s

def solution(play_time, adv_time, logs):
    answer = ''
    # 1: 시간을 초단위로 바꿔서 배열로 저장
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    
    all_time = [0 for _ in range(play_time + 1)]
    
    # 2: log내의 모든 시간에 대해 start, end 값에 1, -1씩 증가
    for log in logs:
        start, end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        
        all_time[start] += 1
        all_time[end] -= 1
        
    # 3: 구간별로 start와 end 사이 사람 수를 채움
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        
    # 4: 전체 범위에서 [i] = [i] + [i-1]로 누적 사람 수를 채움
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
    
    # 5: 가장 사람이 많은 구간을 구함
    most_view, max_time = 0,0
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i-adv_time]:
                most_view = all_time[i] - all_time[i-adv_time]
                max_time = i - adv_time + 1
            
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1
    
    # 6: 5번의 int를 문자열로 바꿔서 리턴
    return int_to_str(max_time)