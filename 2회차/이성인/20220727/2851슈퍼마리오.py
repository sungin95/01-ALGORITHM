score_sum = 0
answer = 0
for i in range(10):
    score = int(input())
    score_sum += score
    if score_sum >= 100:
        present = (score_sum - 100) # 현재
        before = (100 - (score_sum-score)) # 이전값
        if present > before:
            print(100 - before)
        elif present <= before:
            print(100 + present)
        break
else:
    print(score_sum)