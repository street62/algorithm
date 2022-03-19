n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

sums = [0, 0, 0, 0]
largest_sum = 0

for i in range(n):
    for j in range(n):
        sums[0] += nums[i][j]
        sums[1] += nums[j][i]
    sums[2] += nums[i][j]
    sums[3] += nums[n - 1 - i][j]

    temp_max = max(sums)
    if temp_max > largest_sum:
        largest_sum = temp_max
    sums[0], sums[1] = 0, 0

print(largest_sum)
