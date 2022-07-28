# for i in range(65,91):
#     alpha_dict[chr(i)] = 0 # ABCD 딕셔너리로 만듬.
# 변수명은 name에러가 떠서 대충 바꿈.
number = input()
alpha_dict = {
    'A': 3,
    'B': 3, 
    'C': 3, 
    'D': 4, 
    'E': 4, 
    'F': 4, 
    'G': 5, 
    'H': 5, 
    'I': 5, 
    'J': 6, 
    'K': 6, 
    'L': 6, 
    'M': 7, 
    'N': 7, 
    'O': 7, 
    'P': 8, 
    'Q': 8, 
    'R': 8, 
    'S': 8, 
    'T': 9, 
    'U': 9, 
    'V': 9, 
    'W': 10, 
    'X': 10, 
    'Y': 10, 
    'Z': 10
}
second = 0
for char in number:
    second += alpha_dict[char]
print(second)