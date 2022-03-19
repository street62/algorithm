from collections import deque
import itertools

n = int(input())
gotgams = [deque(list(map(int, input().split()))) for _ in range(n)]

m = int(input())
for _ in range(m):
    row, direction, num = map(int, input().split())
    row -= 1
    for _ in range(num):
        if direction == 0:
            gotgams[row].append(gotgams[row].popleft())
        elif direction == 1:
            gotgams[row].appendleft(gotgams[row].pop())
    
start = 0
end = n
res = 0

for i in range(n):
    res += sum(itertools.islice(gotgams[i], start, end))
    if i < n // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(res)