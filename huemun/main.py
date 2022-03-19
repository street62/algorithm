n = int(input())
is_huemun = True
for i in range(n):
    str = input()
    print(str)
    length = len(str)
    print(length)
    for j in range(length):
        left = str[j]
        right = str[length - 1 - j]
        print(left, right)
        if left != right:
            is_huemun = False
    if is_huemun:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
    is_huemun = True




