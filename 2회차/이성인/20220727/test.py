T = int(input())
weight_list = []
height_list = []
dungqi_score = 0 # 덩치
dungqi_list = []

for test_case in range(T):
    a, b = map(int, input().split())
    weight_list.append(a)
    height_list.append(b)
    weight_sort = sorted(weight_list)
    height_sort = sorted(height_list)

for i in range(T):
    weight_rating = weight_sort.index(weight_list[i])
    height_rating = height_sort.index(height_list[i])
    dungqi_score = (weight_rating+height_rating)
    dungqi_list.append(dungqi_score)
dungqi_list_sort = list(reversed(sorted(dungqi_list)))

for i in dungqi_list:
    a = dungqi_list_sort.index(i) + 1
    print(a, end=" ")

