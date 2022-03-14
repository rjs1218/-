import string

Alphabet = list(string.ascii_lowercase)     # 알파벳 모음
input_data = list(input())        # 단어 입력

flag = -1
# 해당 알파벳이
for a in Alphabet:
    for i in range(len(input_data)):
        # 단어에 속한다면
        if a == input_data[i]:
            # 배열 위치 저장
            flag = i
            break
    # 해당 알파벳이 단어에 속한다면 배열 위치를 출력하고, 속하지 않다면 -1 출력.
    print(flag, end=' ')
    flag = -1       # 배열 위치 초기화