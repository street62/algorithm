import sys
# sys.stdin=open("in1.txt", 'r')

n = int(input())
ox = list(map(int, input().split()))
cont = False
current = 0
total = 0

for problem in ox:
    if problem == 0:
        cont = False
    elif problem == 1:
        if cont == False:
            cont = True
            current = 1
        elif cont:
            current += 1
        total += current

print(total)

