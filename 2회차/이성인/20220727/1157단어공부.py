str_ = input()
str_=str_.upper() # 모두 대문자로 변환

alpha_dict = {}
for i in range(65,91):
    alpha_dict[chr(i)] = 0 # ABCD 딕셔너리로 만듬.

for char in str_: # 카운트 과정
    alpha_dict[char] += 1

value_list = list(alpha_dict.values())
alpha_list = list(alpha_dict.keys())
max_value = max(value_list) 
max_key = value_list.index(max_value) # 딕션너리 값을 리스트로 변환해 max_value, max_key를 찾음

one_two = 0
for i in (value_list):
    if i == max_value:
        one_two += 1
        
        if one_two == 2:# 같은게 2개이상 "?"
            print("?")
            break
else:
    print(alpha_list[max_key]) # 중복 없으면 프린트

"""
if cnt.count(max(cnt)) >= 2:
"""

