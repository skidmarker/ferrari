from itertools import permutations
import math


def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers) + 1):
        for num in list(permutations(numbers, i)):
            data = int("".join(num))
            if is_prime_number(data) and data not in answer:
                answer.append(data)

    return len(answer)
