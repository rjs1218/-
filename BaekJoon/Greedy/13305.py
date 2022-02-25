'''
예를 들어, 이 나라에 다음 그림처럼 4개의 도시가 있다고 하자. 원 안에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격이다. 도로 위에 있는 숫자는 도로의 길이를 표시한 것이다. 

제일 왼쪽 도시에서 6리터의 기름을 넣고, 더 이상의 주유 없이 제일 오른쪽 도시까지 이동하면 총 비용은 30원이다. 만약 제일 왼쪽 도시에서 2리터의 기름을 넣고(2x5 = 10원) 다음 번 도시까지 이동한 후 3리터의 기름을 넣고(3x2 = 6원) 다음 도시에서 1리터의 기름을 넣어(1x4 = 4원) 제일 오른쪽 도시로 이동하면, 총 비용은 20원이다. 또 다른 방법으로 제일 왼쪽 도시에서 2리터의 기름을 넣고(2x5 = 10원) 다음 번 도시까지 이동한 후 4리터의 기름을 넣고(4x2 = 8원) 제일 오른쪽 도시까지 이동하면, 총 비용은 18원이다.

각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.
'''

# 기름 값이 제일 싼 도시를 찾아서 남은 거리만큼 기름을 몽땅 넣는다.
# 왼쪽부터 출발하기 때문에, 맨 오른쪽 도시를 제외하고 기름 값이 제일 싼 도시를 찾는다.


city = int(input())                         # 도시 개수
road = list(map(int, input().split()))        # 각 도시를 연결하는 도로의 길이
oilMoney = list(map(int, input().split()))    # 각 도시 기름 값

minimum = oilMoney[0]
for i in range(1, city-1):     # 기름 값이 제일 싼 도시 찾기(맨 오른쪽 도시는 제외)
    if minimum > oilMoney[i]:
        minimum = oilMoney[i]


km = 0      # 남은 도로의 길이
for i in road:
    km += i

money = 0                   # 현재 비용
result = 0                  # 지금까지 든 비용
nowMini = oilMoney[0]       # 지금까지 제일 기름 값이 싼 곳

# 기름 값이 제일 싼 도시라면, 남은 거리만큼 기름을 몽땅 넣는다.
# 그게 아니라면 다음 도시로 가는 도로의 길이만큼 기름을 주유한다.
for i in range(len(road)):
    if oilMoney[i] == minimum:      # 기름 값이 제일 싼 도시를 만난다면
        money = km * minimum
        result += money
        break

    elif nowMini > oilMoney[i]:     # 전 도시보다 기름 값이 더 싸다면
        money = road[i] * oilMoney[i]
        result += money
        km -= road[i]
        nowMini = oilMoney[i]

    else:                           # 다음 도시가 기름 값이 다 비싸다면
        money = road[i] * nowMini
        result += money
        km -= road[i]
    
print(result)   # 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용 출력
