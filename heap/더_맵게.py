import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer

        if len(scoville) == 0:
            break

        second = heapq.heappop(scoville)

        new_s = first + second * 2
        heapq.heappush(scoville, new_s)
        answer += 1

    return -1
