# 시간 입력받기
hour = int(input())

count = 0       # 하루동안 3이 포함될 경우의 수
for h in range(hour+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)