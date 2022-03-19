n, m = map(int, input().split())
num = list(map(int, input().split()))
start, end = 0, 0
sum = num[0]
count = 0

if sum == m:
    count += 1
while start < len(num) and end < len(num) - 1:
    if sum < m:
        end += 1
        sum += num[end]
    elif sum == m or sum > m:
        sum -= num[start]
        start += 1
    if sum == m:
        count += 1

print(count)


    # 처음 인덱스부터 찾았을 때 합이 m이 나왔다면, 시작 인덱스를 +1 하고 끝 인덱스를 +1, +2하면서 m이 나오는지 확인해 보면 시간복잡도를 줄일 수 있을 것 같다!
    # 그러다가 m보다 크면 또 시작 인덱스 1 늘리고... 근데 그럼 끝 인덱스가 늘어나 있는 상황이라서, 이걸 어떻게 해결할지 고민 필요.
    # 이건 고민 안 해도 된다. 예시 보면서 정리해 보기.