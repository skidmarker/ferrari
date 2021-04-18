from itertools import product

def solution(numbers, target):
    case_list = [(x, -x) for x in numbers]
    sum_list = list(map(sum, product(*case_list)))
    return sum_list.count(target)
