from collections import defaultdict


def solution(clothes):
    answer = 1
    clothes_map = defaultdict(list)
    for item, category in clothes:
        clothes_map[category].append(item)
    
    category_count = len(clothes_map.keys())
    for category, items in clothes_map.items():
        answer *= (len(items) + 1)
    
    return answer - 1
