'''
단어의 알파벳에게 숫자의 자릿수만큼 점수를 주고, 딕셔너리에 저장한다.
ex) ABC -> A += 100, B += 10, C -> += 1

알파벳 값들을 리스트로 따로 빼줘,
점수가 큰 순서대로 숫자를 차례차례 곱해준다.

점수들을 합하면 단어의 합 최댓값이 나온다.
'''

import string
import sys

# 알파벳 리스트
alphabet = list(string.ascii_uppercase)

# 알파벳 초기값
zero = []
for i in range(26):
    zero.append(0)

# 각 알파벳과 값을 넣어놓은 딕셔너리
alphabets = dict(zip(alphabet, zero))

# 입력받을 단어 개수 입력
n = int(input())

words = []   # 단어 리스트
# 단어 입력받기
for i in range(n):
    words.append([])
    word = list(sys.stdin.readline().strip())
    # 알파벳에 점수를 주기위해 단어를 뒤집음
    word = word[::-1]
    words[i] = word

score = 1     # 숫자 자릿수만큼 점수주기
# 알파벳에 점수주기
for i in range(n):
    for j in range(len(words[i])):
        alphabets[words[i][j]] += score
        score *= 10
    score = 1

score_list = []     # 알파벳 점수 리스트
# 알파벳 점수를 내림차순으로 정렬해준다.
for val in alphabets.values():
    score_list.append(val)

score_list = sorted(score_list, reverse=True)

n = 9           # 숫자
result = 0      # 결과

# 알파벳 점수 리스트 첫번째가 제일 점수가 큰 알파벳 정보이므로 숫자9부터 차례차례 곱해준다.
for s in score_list:
    s *= n
    result += s
    n -= 1

# 결과 출력
print(result)
