'''
카드 묶음의 합이 더 적은 두 묶음끼리 합치면 최솟값이 나온다

1. 카드 묶음의 합이 더 적은 두 묶음끼리 합쳐준다.
2. 합쳐준 묶음들의 합을 결과값에 더해주고, 기존에 있던 카드 묶음의 리스트를 초기화하고 합쳐준 묶음들을 넣어준다.
3. 카드 묶음의 개수가 1개가 될때까지 1, 2번을 반복한다.
4. 카드 묶음의 개수가 1이 되면 카드 묶음의 합과 결과값을 더해서 출력한다.
'''

import sys

cards = []              # 카드 묶음 리스트
result = 0              # 결과값

n = int(input())        # n개의 카드 묶음

# n개의 카드 묶음 합을 입력받는다.
for i in range(n):
    card = sys.stdin.readline()
    cards.append(int(card))

cards = sorted(cards)       # 카트 묶음 개수를 오름차순으로 정렬

while True:
    # 카드 묶음 개수가 1개라면 비교가 필요가 없다.
    if len(cards) == 1:
        break

    # # 카드 묶음 개수가 2개인 경우, 생각!!!!!
    # elif len(cards) == 2:
    #     pass
    
    # # 카드 묶음 개수가 3개인 경우, 생각!!!!!
    # elif len(cards) == 3:
    #     pass

    '''
    1, 2번 만들어야 됨
    '''
    # 반복문이 돌아가고 카드 묶음 개수가 1개라면 비교가 다 끝난 상태다.
    if len(cards) == 1:
        result += cards[0]
        break


# 최솟값 출력
print(result)
