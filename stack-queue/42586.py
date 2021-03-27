def solution(progresses, speeds):
    answer = []

    start = 0
    while start < len(progresses):
        progress, speed = progresses[start], speeds[start]
        remain = 100 - progress
        
        # 1번째 진행도가 100이 될때까지 다 더해줌
        working_days = remain // speed
        working_days = working_days if remain % speed == 0 else working_days + 1

        for idx, p in list(enumerate(progresses))[start + 1:]:
            s = speeds[idx]
            new_p = p + working_days * s
            progresses[idx] = new_p
        
        additional = 0
        for p in progresses[start + 1:]:
            if p >= 100:
                additional += 1
            else:
                break

        answer.append(1 + additional)
        # 기본적으로 다음 요소, 추가적으로 배포되는 게 있으면 스타트를 넘김
        start += 1 + additional
    
    return answer
