# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    N = len(numbers)
    answer = []
    for i in range(N):
        for j in range(N):
            if i != j:
                sum = numbers[i] + numbers[j]
                if sum not in answer:
                    answer.append(sum)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
