'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

from tracemalloc import start
from turtle import end_fill


room = []

n = int(input())
for i in range(n):
    room.append([])
    time = list(map(int, input().split()))  # 회의 시간을 입력받아 넣어준다.
    room[i] = time

room.sort() # 오름차순 정렬

count = 1   # 회의 개수

# 현재 회의 초기 값 정하기
now = room[0]
for i in room:
    if now[1] > i[1]:
        now = i

# 다음 회의 중 종료 시간이 제일 빠른 회의 택(현재 회의에 넣음)
# 다음 회의는 다음 회의 시작 시간이 현재 회의 종료 시간보다 크거나 같아야 됨

for i in range(len(room)):
    if now[1] <= room[i][0]:
        now = room[i]
        for j in room[i:]:
            if now[1] > j[1]:
                now = j
        count += 1

print(count)
# 제출해서 확인해보기
# -> 반례에서 틀림, 다시해보기
