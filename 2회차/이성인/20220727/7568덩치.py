
# # 저는 하나하나 비교하는 방식이 아니라 
# # 리스트를 정렬시켜서 그 위치 인덱스를 가지고 등수를 매겨서 
# # 몸무게와 키 의 등수합으로 덩치순서를 매겼습니다. 
# # 예를 들어 
# # 5
# # 55 185 (1)
# # 58 183 (2)
# # 88 186 (3)
# # 60 175 (4)
# # 46 155 (5)
# # [46(5),  55(1),  58(2),  60(4),  88(3)] 키 정렬 리스트
# # [155(5), 175(4), 183(2), 185(1), 186(3)] 몸무게 정렬 리슽 
# # 위에 리스트를 만들고 정렬시킨 리스트를 추가로 만들어. 
# # 위치 인덱스를 기반으로 점수를 만들면 
# # (5) 0점, (4) 4 (3) 8 (2) 4 (1) 4 가 나옵니다. 
# # 이 점수를 기반으로 등수를 만들어 출력한 시스템입니다.   

# import sys
# sys.stdin = open("덩치.txt")
# T = int(input())
# weight_list = []
# height_list = []
# dungqi_score = 0 # 덩치 점수
# dungqi_list = [] # 덩치 리스트

# for test_case in range(T): # 받은 값을 리스트로 만듭니다. 
#     a, b = map(int, input().split())
#     weight_list.append(a)
#     height_list.append(b)
# weight_sort = sorted(weight_list)  # 리스트 정렬
# height_sort = sorted(height_list)

# for i in range(T): # 위치 인덱스를 기반으로 점수를 dungqi_list 에 모읍니다. 
#     weight_rating = weight_sort.index(weight_list[i])
#     height_rating = height_sort.index(height_list[i])
#     dungqi_score = (weight_rating+height_rating)
#     dungqi_list.append(dungqi_score)

# dungqi_list_sort = list(reversed(sorted(dungqi_list))) # 덩치리스트 역정렬(큰 점수가 앞에와 큰 점수 순으로 등수를 매기기 위해)
# for dungqi_score in dungqi_list: # 나온 값을 등수로 환산해 제 위치에 출력해 주는 코드입니다. 
#     answer = dungqi_list_sort.index(dungqi_score) + 1
#     print(answer, end=" ")
# # 위 식의 문제점
# """
# 5
# 10 185
# 58 183
# 88 186
# 60 175
# 46 155
# 이렇게 하면 문제가 있다. 
# """


"""
쌤은 비교를 통해서 문제를 해결했고 비교할때 랭크를 정해 주었다. 

이 방버버 꼭 분석해 보자 
"""