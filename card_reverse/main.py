numbers = [i for i in range(1, 21)]
for i in range(10):
    start, end = map(int, input().split())
    reverse_length = (end - start + 1) // 2

    for j in range(reverse_length):
        numbers[start - 1 + j], numbers[end - 1  - j] = numbers[end - 1 - j], numbers[start - 1 + j]
    
for number in numbers:
    print(number, end = " ")
