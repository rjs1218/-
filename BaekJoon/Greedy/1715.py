'''
카드 묶음의 합이 더 적은 두 묶음끼리 합치면 최솟값이 나온다
'''

import sys

cards = []              # 카드 묶음 리스트
sum = 0                 # a와 b 카드 묶음 합
sum_list = []           # 카드 묶음 합 리스트
array_n = 2             # 배열 번호
result = 0              # 카드 묶음 합 결과

n = int(input())        # n개의 카드 묶음

# n개의 카드 묶음 합을 입력받는다.
for i in range(n):
    card = sys.stdin.readline()
    cards.append(int(card))

cards = sorted(cards)       # 카트 묶음 개수를 오름차순으로 정렬

# 카드 묶음 더해주기
sum = cards[0] + cards[1]
sum_list.append(sum)
while True:
    if array_n >= len(cards):       # 배열 번호가 카드 묶음 개수보다 클 경우
        break

    if len(cards) == 3:             # 카드 묶음 개수가 3개일 경우는 비교 필요 없이 합해주면 됨
        sum += cards[array_n]
        sum_list.append(sum)
        break
    
    next = cards[array_n] + cards[array_n+1]    # 두번째 카드 묶음의 합
    sum += cards[array_n]                       # 첫번째 카드 묶음의 합
    if sum > next:
        sum_list.append(next)
        array_n += 2
    else:
        sum_list.append(sum)
        array_n += 1

# 카드 묶음들의 합 최솟값 출력
for n in sum_list:
    result += n
print(result)
