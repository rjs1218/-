import string

small_a = list(string.ascii_lowercase)  # 소문자 알파벳
big_a = list(string.ascii_uppercase)    # 대문자 알파벳

# 알파벳 개수만큼 점수 리스트 만들기
point = []
for i in range(len(small_a)):
    point.append(0)

input_data = input()        # 단어 입력하기.

# 단어의 길이만큼 반복해서
for a in input_data:
    for i in range(len(small_a)):
        # 단어의 각 알파벳이 무슨 알파벳인지 확인 후
        if a == small_a[i] or a == big_a[i]:
            point[i] += 1       # 점수 +1

many = 0
# 가장 많이 사용된 알파벳이 무엇인지 확인하기
for i in range(len(point)):
    if point[i] > many:
        many = point[i]
        many_array = i

# 결과 출력
many_a = big_a[many_array]
point = sorted(point, reverse=True)     # 점수를 내림차순으로 정렬하기.
# 가장 많이 사용된 알파벳 수가 여러개면 '?' 출력
if point[0] == point[1]:            
    print('?')
# 가장 많이 사용된 알파벳 대문자로 출력하기.
else:
    print(many_a)