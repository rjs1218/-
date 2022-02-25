'''
단어 알파벳에게 숫자 자릿수에 해당하는 만큼 숫자를 더해준 후, 딕셔너리에 저장한다.
ex) ABC -> A += 100, B += 10, C -> += 1

딕셔너리의 값을 내림차순으로 정렬 후,
높은 값부터 낮은 값까지 순차적으로 숫자를 곱해준 값들을 더해줘 최댓값을 구한다.
'''

import sys

word_n = int(input())   # 단어 개수

alphabets = {}      # 알파벳 딕셔너리
alphabet_n = []     # 알파벳 점수 리스트
words = []          # 단어 리스트
num = 10            # 자릿수
array_n = 1         # 배열 번호
n_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]      # 숫자 리스트

# 단어 입력받기
for i in range(word_n):
    word = list(sys.stdin.readline().strip())
    words.append(word)

# 단어 알파벳에게 자릿수에 해당하는 만큼 숫자 더해주기
for i in range(word_n):
    for a in words[i]:
        if a in alphabets:
            alphabets[a] += num ** (len(words[i]) - array_n)
            array_n += 1        # 배열 번호 증가
        else:
            alphabets[a] = num ** (len(words[i]) - array_n)
            array_n += 1        # 배열 번호 증가
    array_n = 1

# 딕셔너리 값들을 모아준다.
for val in alphabets.values():
    alphabet_n.append(val)

alphabet_n = sorted(alphabet_n, reverse=True)

# 숫자 곱해주기
array_n = 0

for n in n_list:
    if array_n == len(alphabet_n):
        break
    alphabet_n[array_n] *= n
    array_n += 1

# n개의 단어 합 최댓값 출력
print(sum(alphabet_n))
