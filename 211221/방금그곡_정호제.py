import re

def change_melody(txt):
    txt = re.sub('C#', 'V', txt)
    txt = re.sub('D#', 'W', txt)
    txt = re.sub('F#', 'X', txt)
    txt = re.sub('G#', 'Y', txt)
    txt = re.sub('A#', 'Z', txt)
    return txt

def change_time(txt):
    txt_lst = txt.split(':')
    return int(txt_lst[0])*60 + int(txt_lst[1])

def change_len(time, txt):
    q, r = divmod(time, len(txt))
    return txt*q + txt[:r] if q > 0 else txt[:r]
    
def solution(m, musicinfos):
    answer = []
    target = change_melody(m)
    
    for info in musicinfos:
        info_lst = info.split(',')
        time = change_time(info_lst[1]) - change_time(info_lst[0])
        melody = change_len(time, change_melody(info_lst[3]))
        
        if target in melody:
            answer.append([info_lst[2], time])

    return max(answer, key = lambda x: x[1])[0] if answer else "(None)"