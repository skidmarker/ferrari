from collections import defaultdict

def solution(participant, completion):
    answer = ''
    p_map = defaultdict(int)
    
    for p in participant:
        p_map[p] += 1
    
    for c in completion:
        p_map[c] -= 1
    
    for k, v in p_map.items():
        if v > 0:
            answer = k
            break

    return answer
