"""
https://programmers.co.kr/learn/courses/30/lessons/17681

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)

조건
- 지도를 겹쳐서 얻을 수 있는 "#"과 "공백"으로 이루어진 암호를 리턴하라
1. 지도는 한 변이 n인 정사각형 배열
2. 각 칸은 " "(0) 또는 "#"(1)으로 이루어짐
3. 어느 하나라도 1인 부분은 전체에서도 1이며, 모두 0인 경우 전체에서도 0이다.

알고리즘
1. 배열의 원소를 2진수로 변환
2. or 연산 수행 = 하나라도 1인 경우 1 리턴
3. 1과 0을 각각 "#"과 " "으로 변환

"""
def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1,arr2):
        # 2진수 변환을 위해 bin 함수 사용
        # bin 함수는 앞 2자리가 진수를 표현하기 때문에 2번부터 인덱싱
        num = str(bin(a1|a2)[2:])
        if len(num) < n:
            num = '0' * (n-len(num)) + num
        num = num.replace('1','#')
        num = num.replace('0',' ')
        answer.append(num)
                
    return answer 