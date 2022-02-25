# 선택한 블룹과 양 옆 중 낮은 블룹의 탑의 합을 구해서
# 가장 높은 탑의 합이 나오는 블룹을 선택

n = int(input())                            # N개의 탑
blobs = list(map(int, input().split()))       # 각각의 블롭 탑의 높이

smaller = 0      # 양 옆의 블룹 중 더 낮은 탑의 높이를 가진 블룹
bigger = 0       # 가장 높은 탑의 합

for i in range(1, n-1):
    # 선택한 블룹의 양 옆 중 낮은 탑의 높이를 가지는 블룹 선택
    if blobs[i-1] > blobs[i+1]:
        smaller = blobs[i+1]
    else:
        smaller = blobs[i-1]
    
    # 가장 높은 탑의 합과 선택한 블룹의 탑 높이의 합을 비교
    if bigger < blobs[i] + smaller:
        bigger = blobs[i] + smaller

first = blobs[0]        # 첫번째 블룹 탑 높이
last = blobs[-1]        # 마지막 블룹 탑 높이

# 첫번째 블룹이 제일 클 경우
if first > last:
    if bigger < first:
        bigger = first

# 마지막 블룹이 제일 클 경우
else:
    if bigger < last:
        bigger = last
    
print(bigger)      # 가장 높은 탑의 합 출력
