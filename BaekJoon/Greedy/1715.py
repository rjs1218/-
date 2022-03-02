'''
카드 묶음의 합이 더 적은 두 묶음끼리 합치면 최솟값이 나온다
A = 카드 묶음 합 + 다음 카드 묶음
B = 카드 묶음 합

1. A와 B의 카드 묶음 합이 더 적은 두 묶음끼리 합쳐준다.
2. 합쳐준 묶음들의 합을 결과값에 더해주고, 기존에 있던 카드 묶음의 리스트를 초기화하고 합쳐준 묶음들을 넣어준다.
3. 카드 묶음의 개수가 1개가 될때까지 1, 2번을 반복한다.
4. 카드 묶음의 개수가 1이 되면 카드 묶음의 합과 결과값을 더해서 출력한다.
'''

from re import A
import sys

cards = []              # 카드 묶음 리스트
add = 0                 # 두 묶음의 합
next_add = 0            # 비교할 두 묶음의 합
adds = []               # 묶음 합의 리스트
result = 0              # 결과값

n = int(input())        # n개의 카드 묶음

# n개의 카드 묶음 합을 입력받는다.
for i in range(n):
    card = sys.stdin.readline()
    cards.append(int(card))

cards = sorted(cards)       # 카트 묶음 개수를 오름차순으로 정렬

# 카드 묶음 개수가 1개라면 비교가 필요 없다.
if len(cards) == 1:
    pass

# 카드 묶음 개수가 2개라면 비교가 필요없다.
elif len(cards) == 2:
    add = cards[0] + cards[1]
    result = add

# 카드 묶음 개수가 3개라면 비교가 필요없다.
elif len(cards) == 3:
    add = cards[0] + cards[1]
    result = add + cards[2]

# 카드 묶음 개수가 4개라면 비교가 필요하다.
else:
    add = cards[0] + cards[1]
    result =+ add
    while True:
        '''
        아래는 cards가 4개인 경우 비교가 실행되는 조건문임
        이 조건문이 돌아가면 cards 개수는 0, 1, 2, 3 혹은 4개 이상이 나올 수 있다.
        그리고


        cards 개수가 3개보다 적으면 비교가 더이상 필요없다.
            
        cards 개수가 3개라면, 새로 조건문을 하나 더 만들어야 된다.

        cards 개수가 4개 이상이라면 해당 반복문을 반복하면 된다.

        그리고

        cards = adds 언제 실행해야 되는지 생각하기
        '''
        
        add = cards[0] + cards[1] + cards[2]         # A
        next_add = cards[2] + cards[3]               # B

        if add > next_add:      # B가 더 작을 경우
            adds.append(next_add)
            result += next_add
            for i in range(4):
                cards.pop(i)

        else:                   # A가 더 작을 경우
            adds.append(add)
            result += add
            for i in range(3):
                cards.pop(i)
                
# 최솟값 출력
print(result)
