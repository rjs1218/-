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

A, B = map(int, sys.stdin.readline().split())
count = 1       # 연산 횟수

while True:
    # B의 맨 뒤 숫자가 1이라면
    if B % 10 == 1:
        B = B // 10
        count += 1
    
    # B의 맨 뒤 숫자가 1이 아니라면
    else:
        if B % 2 == 0:      # B가 짝수
            B = B // 2
            count += 1
        
        else:               # B가 홀수
            B = B / 2
            count += 1
    
    # B를 A로 바꿨다면
    if A == B:
        print(count)        # 연산 횟수 출력 후 정지
        break

    # B를 A로 못 바꾼다면
    if A > B:
        print(-1)           # -1 출력 후 정지
        break
