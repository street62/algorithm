def dfs(index, digit):
    global count
    if index == n:
        for i in range(digit):
            print(char[i], end = '')
        print()
        count += 1
        return

    for i in range(1, 26 + 1):
        if num[index] == i:
            char[digit] = (chr(64 + i))
            dfs(index + 1, digit + 1)
        if i >= 10 and num[index] == i // 10 and num[index + 1] == i % 10:
            char[digit] = (chr(64 + i))
            dfs(index + 2, digit + 1)

if __name__ == "__main__":
    num = [int(i) for i in input()]
    n = len(num)
    char = [0] * n
    num.append(-1)
    count = 0
    dfs(0, 0)
    print(count)
    