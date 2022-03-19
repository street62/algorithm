n = int(input())
num_one = list(map(int, input().split()))
m = int(input())
num_two = list(map(int, input().split()))
res = []

i = 0
j = 0

while(i < n or j < m):
    if j == m:
        res.append(num_one[i])
        i += 1
        continue
    elif i == n:
        res.append(num_two[j])
        j += 1
        continue
    if num_one[i] < num_two[j]:
        res.append(num_one[i])
        i += 1
    elif num_one[i] >= num_two[j]:
        res.append(num_two[j])
        j += 1
    
for number in res:
    print(number, end=' ')

