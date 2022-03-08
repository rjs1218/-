'''
1. heap의 pop을 이용해서 카드 묶음 모음에서 가장 적은 카드 묶음끼리 비교한다.
2. 비교한 값을 총 비교 값에 더해주고, 카드 묶음 모음에 다시 넣어준다.
3. 1, 2를 반복한다.
4. 만약 카드 묶음 모음이 하나의 카드 묶음만 있다면, 더 이상 비교할 필요 없다.
'''

import heapq
import sys

cards = []          # 카드 묶음 모음
result = 0          # 비교 횟수 최솟값
min_sum = 0         # 현재 비교값

num = int(input())  # 카드 묶음 개수

for _ in range(num):
    card = int(sys.stdin.readline())    # 카드 묶음
    heapq.heappush(cards, card)

# 카드 묶음 모음이 하나의 카드 묶음만 있다면, 비교할 필요 없다.
if len(cards) == 1:
    pass

else:
    while len(cards) > 1:
        # 카드 묶음에서 가장 적은 카드 묶음끼리 비교
        for _ in range(2):
            min = heapq.heappop(cards)  # 가장 적은 카드 묶음
            min_sum += min              # 현재 비교값

        result += min_sum               # 총 비교 값
        heapq.heappush(cards, min_sum)  # 카드 묶음 모음에 다시 넣기
        min_sum = 0                     # 초기화

# 비교 횟수 최솟값 출력
print(result)