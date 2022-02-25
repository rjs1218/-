'''
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] x B[0] + ... + A[N-1] x B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.
'''

# A를 오름차순, B를 내림차순으로 정렬해서 S값을 구한다.

num = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)                   # 오름차순
B = sorted(B, reverse=True)     # 내림차순

result = 0                      # 결과값
for i in range(num):
    S = A[i] * B[i]
    result += S

print(result)   # 결과값 출력
