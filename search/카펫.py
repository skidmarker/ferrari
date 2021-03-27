def solution(brown, yellow):
    answer = []
    block_count = brown + yellow
    # 가로가 길어야 함
    for horizon in range(block_count, 2, -1):
        if block_count % horizon == 0:
            vertical = block_count // horizon
            if yellow == (horizon - 2) * (vertical - 2):
                answer = [horizon, vertical]
                break
    
    return answer
