'''
replace를 활용하자
'''

# 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_data = input()

# 크로아티아 알파벳 하나씩
for cro in croatia:
    # 비교해서 있으면 하나의 문자 '*'로 바꿔준다.
    input_data = input_data.replace(cro, '*')

# 결과 출력
print(len(input_data))