input_data = list(input().split())

num_r = []        # 뒤집을 숫자
num = []          # 비교할 숫자
for i in range(2):
    # 수를 뒤집기 위해 한 숫자씩 리스트에 넣어주기
    for n in input_data[i]:
        num_r.append(n)
    num_r.reverse()                 # 수 뒤집기
    num.append(''.join(num_r))      # 나눠둔 숫자 합치기
    num_r = []                      # 초기화

A = int(num[0])      # 첫번째 수
B = int(num[1])      # 두번째 수

# 두 수를 비교해서 더 큰 쪽을 출력한다.
if A > B:
    print(A)
else:
    print(B)