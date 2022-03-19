n = int(input())
num_one = list(map(int, input().split()))
m = int(input())
num_two = list(map(int, input().split()))
res = []

i = 0
j = 0

while(i < n - 1 or j < m - 1):
    if num_one[i] <= num_two[j]:
        res.append(num_one[i])
        if i < n - 1:
            i += 1
    if num_one[i] >= num_two[j]:
        res.append(num_two[j])
        if j < m - 1:
            j += 1
    
for number in res:
    print(number, end=' ')

