'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
'''

# S까지 N번의 자연수의 합을 구하고 N을 출력한다.

S = int(input())    # 자연수의 합

num = 1     # 자연수
sum = 0     # 합한 결과
count = 0   # 자연수의 개수

# S까지 N번의 자연수 합하기
while True:
    sum += num      # 자연수 합하기
    num += 1        # 자연수 늘리기

    if sum > S:    # S까지 합하기
        break

    count += 1      # 자연수 개수 추가

print(count)    # N 출력

