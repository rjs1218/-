"""
CodeUp
Python 기초 100제 - 95

기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다.

오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
"바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
"""

#board = [[0 for j in range(20)] for i in range(20)]
#이러한 리스트 생성 방식을 List Comprehensions라고 함.
board = []
for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    board[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(board[i][j], end=' ')
    print()
