import heapq


def solution(operations):
    answer = [0, 0]
    min_q = []
    max_q = []

    for oper in operations:
        action, number = oper.split()
        if action == "D":
            if len(min_q) == 0:
                continue

            if number == "-1":
                data = heapq.heappop(min_q)
                max_q.remove(-data)
            elif number == "1":
                data = heapq.heappop(max_q)
                min_q.remove(-data)
        elif action == "I":
            heapq.heappush(min_q, int(number))
            heapq.heappush(max_q, int(number) * -1)

    if min_q:
        answer = [max(min_q), min(min_q)]
    
    return answer
