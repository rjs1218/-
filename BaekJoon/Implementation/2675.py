import sys

word_n = int(input())        # 단어 개수 입력받기.

words = []                   # 단어
nums = []                    # 반복 출력할 횟수
# 반복 출력할 횟수와 단어 입력받기
for i in range(word_n):
    input_data = sys.stdin.readline().split()
    words.append(input_data[1])        # 단어
    nums.append(int(input_data[0]))    # 반복 출력할 횟수

word = []
# 단어 개수만큼 반복해서
for i in range(len(words)):
    # 단어의 각 알파벳을
    for w in words[i]:
        # 반복 출력할 횟수만큼 늘린다.
        for j in range(nums[i]):
            word.append(w)

    print(''.join(word))    # 늘린 알파벳 출력 
    word = []               # 늘린 알파벳 초기화