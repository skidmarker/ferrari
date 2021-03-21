from collections import defaultdict

    
def solution(genres, plays):
    answer = []
    score_map = defaultdict(int)
    item_map = defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        score_map[genre] += play
        item_map[genre].append((idx, play))
    
    top_genres = sorted(score_map.items(), key=lambda x: x[1], reverse=True)
    for g, _ in top_genres:
        items = sorted(item_map[g], key=lambda x: (x[1], x[0] * -1), reverse=True)[:2]
        answer.extend([i[0] for i in items])

    return answer
