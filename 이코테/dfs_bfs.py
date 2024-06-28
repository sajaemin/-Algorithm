def dfs (graph,V,visited):

    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph,i,visited)

from collections import deque



def bfs(graph, start, visited):

    queue = deque([start])
    
    print(start, end= " ")
    visited[start] = True
    while queue:
        d= queue.popleft()
        for i in graph[d]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end= " ")

visited = [False] * 9

N, M, V = map(int,input().split())

graph =[[] for j in range(N+1)]

for i in range(M):
    
    a = sorted(list(map(int,input().split())))
    # a = list(map(int,input().split()))
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])
    # graph.append(a[:-1])
    


dfs(graph ,V ,visited)


visited = [False] * 9
print()
bfs(graph ,V ,visited)