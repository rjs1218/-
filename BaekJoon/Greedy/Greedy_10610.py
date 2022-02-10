'''
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.
'''

# 입력받은 숫자들로 만들 수 있는 숫자를 모두 만든다.
# 만든 숫자 중 30의 배수이면서 제일 큰 수를 출력한다.
# 30의 배수가 아니라면, -1을 출력한다.

numbers = list(map(int, input()))

numbers.sort()  # 오름차순

unit = 1    # 숫자 자릿수
made_num = 0  # 만든 숫자

# 입력받은 숫자를 이용해서 숫자만들기
for i in range(1, len(numbers)):
    for num in numbers[i:]:
        num *= unit
        unit *= 10
        made_num += num
    
    unit = 1
    # if made_num % 30 == 0:
    #     print(made_num)
    #     break

    # if len(numbers) == i+1:
    #     print(-1)