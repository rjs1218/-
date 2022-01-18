'''
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
'''

# 더한 값과 곱한 값을 비교해서 더 큰 수가 나오는 연산을 수행하면 제일 큰 숫자가 나오기 때문에, 비교를 이용해서 풀었습니다.

def mul(num1, num2):    # 곱셈
    return num1 * num2

def add(num1, num2):    # 덧셈
    return num1 + num2


# 숫자를 문자열로 입력받아 리스트로 나눠줬습니다.
arrayNum = list(input())

# 연산을 위해 문자열을 정수로 만들어준다.
for i in range(len(arrayNum)):
    arrayNum[i] = int(arrayNum[i])

num1 = arrayNum[0]  # 비교할 왼쪽 수
num2 = arrayNum[1]  # 비교할 오른쪽 수

# 곱셈 결과값이 더 크다면 곱셈 사용
if mul(num1, num2) > add(num1, num2):
    num1 = mul(num1, num2)

# 덧셈 결과값이 더 크다면 덧셈 사용
else:
    num1 = add(num1, num2)


for i in range(2, len(arrayNum)):
    num2 = arrayNum[i]
    
    if mul(num1, num2) > add(num1, num2):
        num1 = mul(num1, num2)
    
    else:
        num1 = add(num1, num2)

print(num1) # 결과값 출력