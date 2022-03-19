
def dfs(level, sum):
    global biggest

    if level + table[level][0] >= n:
        if level + table[level][0] > n:
            sum -= table[level][1]
        if sum > biggest:
            biggest = sum
            return
    
    for i in range(level + table[level][0], n):
        dfs(i, sum + table[i][1])

if __name__ == "__main__":
    n = int(input())
    biggest = 0
    table = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        dfs(i, table[i][1])
    
    print(biggest)
