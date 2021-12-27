# https://programmers.co.kr/learn/courses/30/lessons/72414
"""
테스트 1 〉	통과 (1.45ms, 10.5MB)
테스트 2 〉	통과 (6.87ms, 10.6MB)
테스트 3 〉	통과 (15.23ms, 11.2MB)
테스트 4 〉	통과 (185.14ms, 28MB)
테스트 5 〉	통과 (276.67ms, 34.2MB)
테스트 6 〉	통과 (127.65ms, 21.6MB)
테스트 7 〉	통과 (435.78ms, 41.1MB)
테스트 8 〉	통과 (426.29ms, 45.9MB)
테스트 9 〉	통과 (669.33ms, 54.3MB)
테스트 10 〉	통과 (625.78ms, 54.7MB)
테스트 11 〉	통과 (607.82ms, 52.1MB)
테스트 12 〉	통과 (570.80ms, 49.7MB)
테스트 13 〉	통과 (565.84ms, 54.5MB)
테스트 14 〉	통과 (455.06ms, 40.9MB)
테스트 15 〉	통과 (48.21ms, 15.2MB)
테스트 16 〉	통과 (418.43ms, 40.8MB)
테스트 17 〉	통과 (621.98ms, 54.7MB)
테스트 18 〉	통과 (464.89ms, 42.3MB)
테스트 19 〉	통과 (1.59ms, 10.6MB)
테스트 20 〉	통과 (1.49ms, 10.5MB)
테스트 21 〉	통과 (125.40ms, 20.3MB)
테스트 22 〉	통과 (126.36ms, 20.3MB)
테스트 23 〉	통과 (530.96ms, 47.1MB)
테스트 24 〉	통과 (445.00ms, 40.9MB)
테스트 25 〉	통과 (91.48ms, 19.6MB)
테스트 26 〉	통과 (60.28ms, 15MB)
테스트 27 〉	통과 (66.89ms, 17.5MB)
테스트 28 〉	통과 (67.36ms, 17MB)
테스트 29 〉	통과 (61.49ms, 16.8MB)
테스트 30 〉	통과 (48.51ms, 14.2MB)
테스트 31 〉	통과 (48.08ms, 15MB)
"""


def solution(play_time, adv_time, logs):
    # 시간을 초로 변환한다.
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)

    # 모든 play_time 구간을 생성하고 증감을 통해 log별로 곂치는 구간을 체크한다.
    all_time = [0 for i in range(play_time + 1)]
    for l in logs:
        start, end = l.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        # [0, 0, 1, 0, 0, -1, 0, 0]
        all_time[start] += 1
        all_time[end] -= 1

    # 증감을 통해 log별로 곂치는 구간을 기록한다.
    for i in range(1, len(all_time)):
        # [0, 0, 1, 1, 1, 0, 0, 0]
        all_time[i] = all_time[i] + all_time[i - 1]

    # 누적 재생의 합을 구한다. all_time에 기록된 adv_time의 시작과 끝 구간 차이가 클 수록 누적 재생 합이 크다.
    for i in range(1, len(all_time)):
        # [0, 0, 1, 2, 3, 3, 3, 3]
        all_time[i] = all_time[i] + all_time[i - 1]

    # adv_time 동안 누적 재생의 합이 가장 커야 한다.
    mx = -1
    ans = 0
    for i in range(adv_time-1, play_time-1):
        if i >= adv_time:
            if mx < (all_time[i] - all_time[i - adv_time]):
                mx = all_time[i] - all_time[i - adv_time]
                ans = i - adv_time + 1

        else:  # i < adv_time인 구간이므로, 광고 시작 지점은 00:00:00이다.
            if mx < all_time[i]:
                mx = all_time[i]
                ans = i - adv_time + 1
    return sec_to_time(ans)


def time_to_sec(time):
    hour, min, sec = time.split(':')
    return int(hour) * 3600 + int(min) * 60 + int(sec)


def sec_to_time(time):
    hour, time = divmod(time, 3600)
    hour = '0' + str(hour) if hour < 10 else str(hour)

    min, time = divmod(time, 60)
    min = '0' + str(min) if min < 10 else str(min)

    sec = '0' + str(time) if time < 10 else str(time)
    return f'{hour}:{min}:{sec}'


if __name__ == '__main__':
    # 01:30:59
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

    # # 01:00:00
    # play_time = "99:59:59"
    # adv_time = "25:00:00"
    # logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    #
    # # 00:00:00
    play_time = "50:00:00"
    adv_time = "50:00:00"
    logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    print(solution(play_time, adv_time, logs))