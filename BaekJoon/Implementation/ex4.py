data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 존재하는 경우 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))