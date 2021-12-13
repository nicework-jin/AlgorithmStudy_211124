"""
테스트 1 〉	통과 (0.18ms, 10.3MB)
테스트 2 〉	통과 (0.17ms, 10.4MB)
테스트 3 〉	통과 (0.17ms, 10.2MB)
테스트 4 〉	통과 (0.18ms, 10.3MB)
테스트 5 〉	통과 (0.18ms, 10.2MB)
테스트 6 〉	통과 (0.18ms, 10.2MB)
테스트 7 〉	통과 (0.18ms, 10.2MB)
테스트 8 〉	통과 (0.18ms, 10.2MB)
테스트 9 〉	통과 (0.18ms, 10.3MB)
테스트 10 〉	통과 (0.18ms, 10.3MB)
테스트 11 〉	통과 (0.18ms, 10.3MB)
테스트 12 〉	통과 (0.18ms, 10.2MB)
테스트 13 〉	통과 (0.18ms, 10.3MB)
테스트 14 〉	통과 (0.18ms, 10.2MB)
테스트 15 〉	통과 (0.26ms, 10.2MB)
테스트 16 〉	통과 (0.19ms, 10.2MB)
테스트 17 〉	통과 (0.21ms, 10.3MB)
테스트 18 〉	통과 (0.22ms, 10.2MB)
테스트 19 〉	통과 (0.26ms, 10.3MB)
테스트 20 〉	통과 (0.28ms, 10.2MB)
테스트 21 〉	통과 (0.26ms, 10.3MB)
테스트 22 〉	통과 (0.28ms, 10.3MB)
테스트 23 〉	통과 (0.18ms, 10.2MB)
테스트 24 〉	통과 (0.21ms, 10.2MB)
테스트 25 〉	통과 (0.20ms, 10.2MB)
테스트 26 〉	통과 (0.18ms, 10.2MB)
"""

import re


def solution(id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    # ...!@BaT#*..y.abcdefghijklm  ->  ...!@bat#*..y.abcdefghijklm
    id = id.lower()

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    # ...!@bat#*..y.abcdefghijklm  ->  ...bat..y.abcdefghijklm
    id = re.sub('[^a-z\d\-\_\.]', '', id)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    # ...bat..y.abcdefghijklm  ->  .bat.y.abcdefghijklm
    id = re.sub('\.+', '.', id)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    # .bat.y.abcdefghijklm  ->  bat.y.abcdefghijklm
    id = re.sub('^\.|\.$', '', id)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(id) == 0:
        id += 'a'

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(id) >= 16:
        id = id[:15]

    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if id and id[-1] == '.':
        id = id[:-1]

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다
    while len(id) < 3:
        id += id[-1]
    return id


if __name__ == '__main__':
    # "bat.y.abcdefghi"
    new_id = "...!@BaT#*..y.abcdefghijklm"

    # # "z--"
    # new_id = "z-+.^."

    # # "aaa"
    # new_id = "=.="

    # # "123_.def"
    # new_id = "123_.def"

    # "abcdefghijklmn"
    # new_id = "abcdefghijklmn.p"
    print(solution(new_id))
