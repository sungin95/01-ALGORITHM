str_ = "O"+input() # "O"는 계산산의 이유로 임의로 넣어줬습니다. 
n = len(str_)
list_ = ["c=", "c-","dz=","d-","lj","nj","s=","z="]
cnt = 0
for c in list_:
    b = 0
    a = 0
    while a >= 0:
        b = a
        a = str_.find(f"{c}",b+1)
        cnt += 1
print(n-cnt-1+8)




