'''
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
'''

# B를 A로 바꿔보자.
# 맨 뒤 숫자가 1이 아니라면 2를 나눠주고
# 맨 뒤 숫자가 1이라면 맨 뒤 숫자를 없앤다.
# 결과 값이 A보다 작다면 -1을 출력한다.

import sys

A, B = sys.stdin.readline().split()
count = 1   # 연산 횟수

while True:
    # 맨 뒤 숫자가 1이라면
    if B[-1] == '1':
        B = B[:-1]      # 맨 뒤 숫자 없애기
        count += 1      # 연산 횟수 늘려주기

    # B가 짝수이고, 맨 뒤 숫자가 1이 아니라면
    elif int(B) % 2 == 0 and B[-1] != '1':
        B = int(B) // 2
        B = str(B)      # 문자열로 다시 바꿔주기
        count += 1      # 연산 횟수 늘려주기

    # B가 홀수이고, 맨 뒤 숫자가 1이 아니라면
    else:
        B = int(B) / 2
        B = str("{:g}".format(B))
        count += 1      # 연산 횟수 늘려주기
    
    # A를 B로 바꿀 수 있다면 연산 횟수 출력 후 정지
    if A == B:
        print(count)
        break
    
    # A를 B로 바꿀 수 없다면 -1 출력 후 정지
    elif A > B:
        print(-1)
        break
