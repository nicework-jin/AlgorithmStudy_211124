"""
https://programmers.co.kr/learn/courses/30/lessons/42576

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.15ms, 10.3MB)
테스트 4 〉	통과 (0.30ms, 10.4MB)
테스트 5 〉	통과 (0.28ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (24.89ms, 21.7MB)
테스트 2 〉	통과 (36.60ms, 25.1MB)
테스트 3 〉	통과 (40.03ms, 27.6MB)
테스트 4 〉	통과 (49.33ms, 33.8MB)
테스트 5 〉	통과 (48.24ms, 34MB)
"""


def solution(participant_list, completion_list):
    not_completion_dict = {}
    for participant in participant_list:
        not_completion_dict[participant] = not_completion_dict.get(participant, 0) + 1

    for completion in completion_list:
        not_completion_dict[completion] -= 1

    for k, v in not_completion_dict.items():
        if v == 1:
            return k


if __name__ == "__main__":
    # leo
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    # vinko
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]

    # misalv
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    print(solution(participant, completion))
