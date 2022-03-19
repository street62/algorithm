def dfs(sum, index, num):
    global cnt
    if num > coins[index][1]:
        return
    if sum == t:
        cnt += 1
        return
    dfs(sum + coins[index][0], index, num + 1)
    if index == len(coins) - 1:
        return
    dfs(sum + coins[index + 1][0], index + 1, 1)
    
if __name__ == "__main__":
    cnt = 0
    t = int(input())
    n = int(input())
    coins = []
    for _ in range(n):
        coins.append(list(map(int, input().split())))
    coins.sort(reverse=True)
        
    dfs(0, 0, 0)
    print(cnt)