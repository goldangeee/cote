graph = {
    1 : [2, 3],
    2 : [1, 4],
    3 : [1],
    4 : [2]
}
def sol(graph,current_node,visited = None):
    if visited is None:
        visited = []
    visited.append(current_node)
    print(current_node)
    for node in graph[current_node]:
        if node not in visited:
            sol(graph,node,visited)


sol(graph,1)
# 출력
# 1
# 2
# 4
# 3