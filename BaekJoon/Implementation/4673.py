# 생성자를 만드는 함수 d
def d(n):
    temp = 0
    for num in str(n):
        temp += int(num)
    
    return n + temp

nums = list(range(1, 10001))    # 1 ~ 10000
c_nums = set()                  # 생성자 모음

# 1 ~ 10000까지의 숫자 중에서
for num in nums:
    c_num = d(num)
    c_nums.add(c_num)           # 생성자 삽입

result = set(nums) - c_nums     # 생성자 제거
# 생성자 제외한 숫자 출력하기.
for self_num in sorted(result):
    print(self_num)