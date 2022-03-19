def dfs(level, sum):
    global cnt
    if level == n:
        if sum == t:
            cnt += 1
            return
        return
    if sum > t:
        return
    for i in range(coins[level][1] + 1):
        dfs(level + 1, sum + coins[level][0] * i)
    
if __name__ == "__main__":
    cnt = 0
    t = int(input())
    n = int(input())
    coins = []
    for _ in range(n):
        coins.append(list(map(int, input().split())))
    coins.sort(reverse=True)
    
    dfs(0, 0)
    print(cnt)