from collections import deque

maze = [list(map(int, input().split())) for _ in range(7)]
check = [[0]*7 for _ in range(7)]
route = deque()

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
start = [0, 0]
res = 0
route.append(start)
level = 0
is_found = False

while True:
    for _ in range(len(route)):
        now = route.popleft()
        if now == [6, 6]:
            res = level
            is_found = True
            break
        for i in range(4):
            new_y = now[0] + dy[i]
            new_x = now[1] + dx[i]
            if 0 <= new_y <= 6 and 0 <= new_x <= 6:
                if check[new_y][new_x] == 0 and maze[new_y][new_x] == 0:
                    route.append([new_y, new_x])
                    check[new_y][new_x] = 1
    level += 1
    if is_found:
        break
    if len(route) == 0 and res == 0:
        res = -1
        break

print(res)

