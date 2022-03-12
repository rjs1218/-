def x(number):
    result = 99     # 100보다 크면, 기본적으로 99개의 한수를 가진다.

    # 100보다 작으면 모두 한수이다.
    if number < 100:
        return number

    # 100보다 크면 등차수열인지 확인해야 한다.
    else:
        for i in range(100, number+1):
            # 각 자릿수의 수를 리스트에 넣는다.
            num = []
            for n in str(i):
                num.append(int(n))
            # 등차수열 확인
            if num[2] - num[1] == num[1] - num[0]:
                result += 1

        return result

input_data = int(input())
print(x(input_data))