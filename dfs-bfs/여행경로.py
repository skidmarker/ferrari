from collections import defaultdict


def solution(tickets):
    routes = defaultdict(list)
    for k, v in tickets:
        routes[k].append(v)

    for r in routes:
        routes[r].sort()

    answer = dfs(routes)

    return answer


def dfs(routes):
    stack = ["ICN", ]
    path = []

    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))

    return path[::-1]
