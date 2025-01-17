graph = {
    1 : [2, 3],
    2 : [4],
    3 : [],
    4 : []
}

def sol(graph):
    print(1)
    for x in graph[1]:
        sol()
            
sol(graph)
# 출력
# 1
# 2
# 4
# 3