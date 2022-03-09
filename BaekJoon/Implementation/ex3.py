# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
cases = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0

for case in cases:
    # 이동하고자 하는 위치 확인
    next_row = row + case[0]
    next_column = column + case[1]

    # 이동이 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)