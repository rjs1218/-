n = int(input())                    # n x n 공간 입력
direction = input().split()         # 방향 입력

directions = ['U', 'D', 'L', 'R']   # 상하좌우
x_dir = [-1, 1, 0, 0]               # 상하좌우 x 좌표
y_dir = [0, 0, -1, 1]               # 상하좌우 y 좌표
x, y = 1, 1                         # 현재 좌표

for dir in direction:
    for i in range(len(directions)):
        if dir == directions[i]:    # 이동 후 좌표 구하기.
            nx = x + x_dir[i]
            ny = y + y_dir[i]
        
    # 좌표가 n x n 공간 밖으로 이동했다면 이동하지 않는다.
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    
    x, y = nx, ny                   # 이동 수행

print(x, y)