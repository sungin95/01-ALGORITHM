def Rev(num):
    num_str = str(num)
    num_str_rev = ""
    num_rev = ""
    for char in num_str[::-1]:
        num_str_rev += (char)
    num_rev = int(num_str_rev)
    return num_rev
a, b = map(int, input().split())

print(Rev(Rev(a) + Rev(b)))