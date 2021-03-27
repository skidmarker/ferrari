import heapq


def solution(jobs):
    answer = 0
    time = 0
    last = -1
    waiting_list = []
    count = 0

    while count < len(jobs):
        for start_sec, working_sec in jobs:
            if last < start_sec <= time:
                heapq.heappush(waiting_list, (working_sec, start_sec))

        # 대기중인 작업이 없으면 다음으로
        if not waiting_list:
            time += 1
            continue

        count += 1
        last = time
        working_sec, start_sec = heapq.heappop(waiting_list)
        time += working_sec
        answer += (time - start_sec)

    return answer // len(jobs)
