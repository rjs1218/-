'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''


cal = input()
cal = list(cal[::-1])   # 거꾸로 바꿔주기

size = 0                # n자리 숫자
num = 0                 # 모임에 들어갈 숫자
numlist = []            # 숫자 리스트
callist = []            # 연산 리스트
symbol = []             # 기호 리스트

# 숫자 합치고 연산 리스트에 넣어주는 과정
for i in range(len(cal)):
    if cal[i] != '-' and cal[i] != '+':     # i가 숫자라면 n자리 숫자만큼 곱해주기
        size += 1

        cal[i] = int(cal[i])
        if size == 1:
            cal[i] *= 1
        elif size == 2:
            cal[i] *= 10

        num += cal[i]           # 숫자 합치기
    
    if cal[i] == '-' or cal[i] == '+':
        size = 0                # n자리 초기화
        numlist.append(num)     # 숫자 리스트에 숫자 넣어주기
        callist.append(num)     # 연산 리스트에 숫자 넣어주기
        num = 0                 # 숫자 초기화
        callist.append(cal[i])  # 연산 리스트에 기호 넣어주기
        symbol.append(cal[i])
    
    if i+1 == len(cal):         # 마지막 차례라면 연산 리스트에 넣어주기
        numlist.append(num)
        callist.append(num)

callist = callist[::-1]         # 정상적으로 바꿔주기(거꾸로 바꾼 것을 원래대로)
numlist = numlist[::-1]
symbol = symbol[::-1]

# A - B + C와 같이 + 기호 앞에 - 기호가 있다면
# -(B + C)처럼 괄호로 묶어주고
# - 기호 앞에 - 기호이 있다면
# 그대로 계산해준다.

# + ... -일 상황 -> 그대로 연산
# - -일 상황 -> 그대로 연산
# - +일 상황 -> +를 -로 바꿔주고 연산

# 조건에 맞게 연산 리스트에 있는 연산들을 수행만하면 문제 clear
print(callist, '\n')
print(numlist, '\n')
print(symbol)
