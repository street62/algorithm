def dfs(index, digit):
    global count
    if index >= len(num):
        for i in char:
            print(i, end = '')
        print()
        count += 1
        return
    if index + digit > len(num):
        return
    current = 0
    for i in range(digit):
        current = current * 10 + int(num[index + i])
    if 1 <= current <= 26:
        char.append(chr(64 + current))
        dfs(index + digit, 1)
        char.pop()
        dfs(index, digit + 1)
    
if __name__ == "__main__":
    num = [int(i) for i in input()]
    char = []
    count = 0
    dfs(0,1)
    print(count)