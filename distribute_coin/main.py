def dfs(index, one, two, three):
    global res
    if index == n:
        if one == two or one == three or two == three:
            return
        largest = max(one, two, three)
        smallest = min(one, two, three)
        temp = largest - smallest
        if temp < res:
            res = temp
        return
    dfs(index + 1, one + numbers[index], two, three)
    dfs(index + 1, one, two + numbers[index], three)
    dfs(index + 1, one, two, three + numbers[index])

if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    res = 2147483647
    dfs(0, 0, 0, 0)
    print(res)