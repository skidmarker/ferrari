def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_sum = second_sum = third_sum = 0

    for idx, a in enumerate(answers):
        if a == first[idx % 5]:
            first_sum += 1        
        if a == second[idx % 8]:
            second_sum += 1        
        if a == third[idx % 10]:
            third_sum += 1
    
    max_sum = max(first_sum, second_sum, third_sum)
    for idx, data in enumerate([first_sum, second_sum, third_sum]):
        if data == max_sum:
            answer.append(idx + 1)

    return answer
