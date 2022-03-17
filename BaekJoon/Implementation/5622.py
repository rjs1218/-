input_data = list(input())

sec = [3, 4, 5, 6, 7, 8, 9, 10]     # 다이얼이 걸리는 시간
result = 0
for i in range(len(input_data)):
    num = ord(input_data[i]) - ord('A') + 1
    
    if 0 < num < 4:             # ABC
        result += sec[0]
    elif 3 < num < 7:           # DEF
        result += sec[1]
    elif 6 < num < 10:          # GHI
        result += sec[2]
    elif 9 < num < 13:          # JKL
        result += sec[3]
    elif 12 < num < 16:         # MNO
        result += sec[4]
    elif 15 < num < 20:         # PQRS
        result += sec[5]
    elif 19 < num < 23:         # TUV
        result += sec[6]
    else:                       # WXYZ
        result += sec[7]

print(result)       # 결과 출력