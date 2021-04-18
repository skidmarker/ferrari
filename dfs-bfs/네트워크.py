def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]
    for idx in range(n):
        if visited[idx] is False:
            dfs(n, computers, idx, visited)
            answer += 1

    return answer

def dfs(n, computers, idx, visited):
    visited[idx] = True
    for connect in range(n):
        if connect != idx and computers[idx][connect] == 1:
            if visited[connect] is False:
                dfs(n, computers, connect, visited)
