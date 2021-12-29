n = int(input())
student = input().split()

for i in range(n):
    student[i] = int(student[i])

small = student[0]

for i in range(1, n):
    if small > student[i]:
        small = student[i]

print(small)