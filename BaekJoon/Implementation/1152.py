input_data = input()
empty = ' '         # 빈 문자열
first = 0           # 첫 문자라면 0, 아니라면 1
result = 0

list_data = []
# 입력받은 문자열을 각각 리스트에 넣는다.
for s in input_data:
    list_data.append(s)

for i in range(len(input_data)):
    # 빈 문자열이라면
    if list_data[i] == empty:
        first = 0           # 다음 문자는 첫 문자이다
        pass                # 넘긴다.
    # 빈 문자열이 아니라면
    else:
        # 첫 문자라면
        if first == 0:
            result += 1     # 단어 +1
            first = 1       # 다음 문자는 첫 문자가 아님
        # 첫 문자가 아니라면
        else:
            pass

# 단어 개수 출력
print(result)