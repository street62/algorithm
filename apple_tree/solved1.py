n = int(input())
apples = [list(map(int, input().split())) for _ in range(n)]
start, end = n // 2, (n // 2) + 1
total = sum(apples[0][start:end])

for i in range(1, n):
    if i <= n // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
    total += sum(apples[i][start:end])

print(total)