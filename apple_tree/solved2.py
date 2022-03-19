from collections import deque

n = int(input())
apples = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
now = [n//2, n//2]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
deq = deque()
res = 0
level = 0

deq.append(now)
check[now[0]][now[1]] = 1
res += apples[now[0]][now[1]]
sequence = 0
require = 4


while True:
    if level == n // 2:
        break
    now = deq.popleft()
    for i in range(4):
        sequence += 1
        temp = [now[0]+dy[i], now[1]+dx[i]]
        if check[temp[0]][temp[1]] == 0:
            deq.append(temp)
            check[temp[0]][temp[1]] = 1
            res += apples[temp[0]][temp[1]]
    if sequence == require:
        sequence = 0
        require = (level + 1) * 16
        level += 1

print(res)
            