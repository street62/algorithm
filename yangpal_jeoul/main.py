def dfs(index, sum):
    if index == k:
        if sum <= 0:
            return
        sums.add(sum)
        return
    
    dfs(index + 1, sum + nums[index])
    dfs(index + 1, sum)
    dfs(index + 1, sum - nums[index])

if __name__ == "__main__":
    k = int(input())
    nums = list(map(int, input().split()))
    s = sum(nums)
    sums = set()

    dfs(0, 0)

    print(s - len(sums))
    