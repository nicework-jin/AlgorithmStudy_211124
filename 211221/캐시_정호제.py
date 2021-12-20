# '''
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (59.86ms, 17.6MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.04ms, 10.3MB)
# 테스트 14 〉	통과 (0.11ms, 10.3MB)
# 테스트 15 〉	통과 (0.09ms, 10.2MB)
# 테스트 16 〉	통과 (0.12ms, 10.2MB)
# 테스트 17 〉	통과 (0.13ms, 10.3MB)
# 테스트 18 〉	통과 (0.32ms, 10.3MB)
# 테스트 19 〉	통과 (0.45ms, 10.3MB)
# 테스트 20 〉	통과 (0.59ms, 10.3MB)
# '''
# from collections import deque

# def solution(cacheSize, cities):
#     answer = 0
#     cache = deque([], maxlen=cacheSize)
    
#     for city in cities:
#         city = city.lower()
#         if city in cache:
#             del cache[cache.index(city)]
#             cache.append(city)
#             answer += 1
#         else:
#             cache.append(city)
#             answer += 5

#     return answer

def solution(cacheSize, cities):
    time = 0
    cache = []
    cities = [city.lower() for city in cities]
    if cacheSize != 0:
        for city in cities:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    time += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    time += 5
    else: time += len(cities) * 5
    return time