'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''


cal = input()
cal = list(cal[::-1])   # 거꾸로 바꿔주기(n의 자리의 숫자인지 알아내기 위해)

size = 0                # n자리 숫자
num = 0                 # 리스트에 들어갈 숫자
numlist = []            # 숫자 리스트
symbol = []             # 기호 리스트

# 숫자를 합치고, 연산과 숫자를 각 리스트에 넣어주는 과정
for i in range(len(cal)):
    if cal[i] != '-' and cal[i] != '+':     # i가 숫자라면 n자리 숫자만큼 곱해주기
        size += 1

        cal[i] = int(cal[i])
        if size == 1:           # 1의 자리
            cal[i] *= 1
        elif size == 2:         # 10의 자리
            cal[i] *= 10
        elif size == 3:         # 100의 자리
            cal[i] *= 100
        elif size == 4:         # 1000의 자리
            cal[i] *= 1000
        else:                   # 10000의 자리
            cal[i] *= 10000

        num += cal[i]           # 숫자 합치기
    
    if cal[i] == '-' or cal[i] == '+':      # i가 기호라면
        size = 0                # n자리 초기화
        numlist.append(num)     # 숫자 리스트에 숫자 넣어주기
        num = 0                 # 숫자 초기화
        symbol.append(cal[i])   # 기호 리스트에 기호 넣어주기
    
    if i+1 == len(cal):         # 마지막 차례라면 연산 리스트에 넣어주기
        numlist.append(num)

numlist = numlist[::-1]         # 정상적으로 바꿔주기(거꾸로 바꾼 것을 원래대로)
symbol = symbol[::-1]


result = numlist[0]     # 결과값
index = 1               # 현재 인덱스

for i in symbol:    # 이번 연산이 -로 시작한다면 모든 연산을 -로 구해준다.
    if i == '-':
        while True:
            for j in numlist[index:]:
                result -= j

            break
        break

    else:           # 연산이 +로 시작한다면 이번 연산만 +로 구해준다.
        result += numlist[index]
        index += 1

print(result)