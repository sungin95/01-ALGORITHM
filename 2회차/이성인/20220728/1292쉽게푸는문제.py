gauss_dict = {}
for n in range(1,100):  # value 값 최대 1000까지 가우스 덧셈법칙 딕셔너리
    if (n*(n+1)//2) <= 1000:
        gauss_dict[f"{n}"] = (n*(n+1)//2)
    else:
        gauss_dict[f"{n}"] = (n*(n+1)//2)
        break 

a,b = map(int, input().split())
sum_ = 0
for i in range(a,b+1):
    for j in gauss_dict:
        if gauss_dict[j] >= i:
            sum_ += int(j)
            break
print(sum_)