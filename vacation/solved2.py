
def dfs(level, sum):
    global biggest

    if level == n:
        if sum > biggest:
            biggest = sum
        return
    if level + table[level][0] <= n:
        dfs(level + table[level][0], sum + table[level][1])
    dfs(level + 1, sum)

if __name__ == "__main__":
    n = int(input())
    biggest = 0
    table = [list(map(int, input().split())) for _ in range(n)]
    dfs(0, 0)
    
    print(biggest)
