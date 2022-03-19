n = int(input())
gotgams = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    row, direction, num = map(int, input().split())
    row -= 1
    for _ in range(num):
        if direction == 0:
            temp = gotgams[row][0]
            for i in range(n - 1):
                gotgams[row][i] = gotgams[row][i + 1]
            gotgams[row][n - 1] = temp
        elif direction == 1:
            temp = gotgams[row][n - 1]
            for i in range(n - 1):
                gotgams[row][n - 1 - i] = gotgams[row][n - 2 - i]
            gotgams[row][0] = temp
    
start = 0
end = n
res = 0

for i in range(n):
    res += sum(gotgams[i][start:end])
    if i < n // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(res)