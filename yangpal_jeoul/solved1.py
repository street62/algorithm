def dfs(index, sum):
    if index == k - 1:
        if sum < 0:
            return
        if check[sum - 1] == 0: # == 써야 하는 곳에 = 쓰지 말기
            check[sum - 1] = 1
            return
        return # 마지막 return 까먹지 말기
    
    dfs(index + 1, sum + nums[index + 1])
    dfs(index + 1, sum)
    dfs(index + 1, sum - nums[index + 1])

if __name__ == "__main__":
    k = int(input())
    cnt = 0
    nums = list(map(int, input().split()))
    check = [0]*sum(nums)

    dfs(-1, 0)
    for i in check:
        if i == 0:
            cnt += 1
    print(cnt)