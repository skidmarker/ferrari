def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        if i == j:
            answer.append(array[i - 1:][k - 1])
        else:
            sorted_data = sorted(array[i - 1:j])
            answer.append(sorted_data[k - 1])
    return answer
