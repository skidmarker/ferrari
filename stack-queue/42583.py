from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while len(truck_weights) != 0 or len(bridge) != 0:
        bridge.popleft()

        tmp = 0
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                tmp = truck_weights.popleft()

            bridge.append(tmp)

        answer += 1
    
    return answer

