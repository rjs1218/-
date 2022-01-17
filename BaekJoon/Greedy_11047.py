'''
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''

count = 0

# N은 동전의 종류 개수, K는 동전의 종류를 이용해서 만들고자 하는 값.
N, K = map(int, input().split())
arrayN = []

# 동전 종류 개수만큼 동전 종류를 입력 받아, arrayN에 넣는다.
for i in range(N):
    arrayN.append([])
    arrayN[i] = int(input())


for coin in arrayN[::-1]:    # 배열 역순으로 하기. -> [::-1]
    count += K // coin     # K값을 만드는데 필요한 동전 종류의 개수
    K %= coin

# K를 만드는데 필요한 동전 개수의 최솟값을 출력한다.
print(count)