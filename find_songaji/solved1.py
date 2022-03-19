s, e = map(int, input().split())
remain = e - s
count = 0

while (remain != 0):
    if 0 < remain < 4:
        remain -= 1
        count += 1
    elif remain >= 4:
        remain -= 5
        count += 1
    else:
        remain += 1
        count += 1

print(count)
