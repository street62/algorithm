from collections import deque

s, e = map(int, input().split())
MAX = 10000
is_found = False
number_line = [-1] * (MAX + 1)
dq = deque()
dq.append(s)
number_line[s] = 0
res = 0

if s == e:
    is_found = True

while (is_found == False):
    now = dq.popleft()
    for next in (now + 1, now - 1, now + 5):
        if number_line[next] == -1 and 1 < next < MAX:
            number_line[next] = number_line[now] + 1
            dq.append(next)
            if next == e:
                res = number_line[next]
                is_found = True
                break

print(res)
