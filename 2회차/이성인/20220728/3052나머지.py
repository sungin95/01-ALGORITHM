rest_list = []
for _ in range(10):
    num = int(input())
    rest = num % 42
    rest_list.append(rest)
print(len(list(set(rest_list))))