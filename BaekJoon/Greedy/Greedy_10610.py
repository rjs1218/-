'''
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.
'''

# 30 60 90 120 150 180 210 240 270 300
# 마지막 숫자는 항상 0
# 숫자들을 더하면 3의 배수가 나옴

# 10의 5승까지 숫자를 입력할 수 있기 때문에 int로는 출력이 안 됨, 숫자를 출력할 때 문자열로 변경해야 됨.

numbers = list(map(int, input()))
# 내림차순으로 정렬
numbers = sorted(numbers, reverse=True)
number = []

# 30의 배수인 경우
if sum(numbers) % 3 == 0 and \
numbers[-1] == 0:
    for i in range(len(numbers)):
        # 문자열로 바꾸기
        number.append(str(numbers[i]))

    # 문자열 합치기
    number = ''.join(number)    
    print(number)   # 가장 큰 수 출력

# 30의 배수가 아닌 경우
else:
    print(-1)
