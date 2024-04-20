# dfs

def dfs(visited,graph,node):
  print(node , end=" ")
  visited.add(node)

  for neighbor in graph[node]:
    if neighbor not in visited:
      dfs(visited,graph,neighbor)


graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited = set()
dfs(visited,graph,'B')

from collections import deque

def bfs(graph,start):
  visited = set()
  queue = deque([start])
  visited.add(start)

  while queue:
    node = queue.popleft()
    print(node , end=" ")

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}

bfs(graph, 0)
