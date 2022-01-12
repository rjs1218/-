"""
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
"""

board = []

# 0으로 꽉 찬, 20 x 20 바둑판 만들기(좌표 값이 1, 1부터 시작하기 때문에 20 x 20으로 만듦)
for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

for i in range(19):
    boardNum = list(map(int, input().split()))   # 입력 값을 리스트 형태로 넣음
    for j in range(19):
        board[i+1][j+1] = boardNum[j]    # 1, 1 좌표부터 순차 적으로 입력 값을 넣음

# 반복 횟수 입력 받음
num = int(input())

for i in range(num):
    x, y = map(int, input().split())
    for j in range(1,20):       # 좌표값이 0이면 1로, 1이면 0으로 바꿔주기
        if board[j][y] == 0:
            board[j][y] = 1
        else:
            board[j][y] = 0
        
        if board[x][j] == 0:
            board[x][j] = 1
        else:
            board[x][j] = 0

# 출력하기
for i in range(1, 20):
    for j in range(1, 20):
        print(board[i][j], end=' ')
    print()
