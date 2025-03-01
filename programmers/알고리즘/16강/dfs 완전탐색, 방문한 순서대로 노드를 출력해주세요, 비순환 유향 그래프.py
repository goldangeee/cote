from collections import deque

graph = {
    1 : [2, 3],
    2 : [4],
    3 : [],
    4 : []
}

# 재귀호출을 이용한 풀이
def sol(graph,current_node = None):
    if current_node is None:
        current_node = 1
    print(current_node)
    for node in graph[current_node]:
        sol(graph,node)

sol(graph)
# 출력
# 1
# 2
# 4
# 3

## 데크를 이용한 풀이
# def sol(graph):
#     d = deque([1])
#     while d:
#         current_node = d.popleft()
#         print(current_node)
#         d = deque(graph[current_node]) + d