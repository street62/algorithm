str = input()
num = 0
for i in range(len(str)):
    if 48 <= ord(str[i]) <= 57:
        num = num * 10 + int(str[i])
print(num)

res = 1
for i in range(2, num + 1):
    exponent = 0
    while (num % i == 0):
        num = num // i
        exponent += 1
    res *= (exponent + 1)
    if num == 1:
        break

print(res)