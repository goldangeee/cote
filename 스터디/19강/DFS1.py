graph = {
    1 : [2, 3],
    2 : [4],
    3 : [],
    4 : []
}

def sol(graph):
    print(1)

    def sol2(graph,x):
        for a in graph[x]:
            print(a)
            if graph[a]:
                sol2(graph,a)
    
    sol2(graph,1)
        
sol(graph)
'''
def dfs(graph, node):
    print(node)
    
    for nei_node in graph[node]:
        dfs(graph, nei_node)

def sol(graph):
    dfs(graph, 1)

sol(graph)
'''
# 출력
# 1
# 2
# 4
# 3