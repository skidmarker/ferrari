from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(idx, p) for idx, p in enumerate(priorities)])

    while q:
        idx, p = q.popleft()
        put_flag = False
        
        for p2 in q:
            if p2 > p:
                put_flag = True
                break
        
        if put_flag:
            q.append((idx, p))
        else:
            answer += 1
            if location == idx:
                break

    return answer
