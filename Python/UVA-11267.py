from sys import *

def makeSet(v):
   p[v], rango[v] = v, 0

def findSet(v):
   ans = None
   if v == p[v]: ans = v
   else:
      p[v] = findSet(p[v])
      ans = p[v]
   return ans

def unionSet(u, v):
   u, v = findSet(u), findSet(v)
   if u != v:
      if rango[u] < rango[v]: u, v = v, u
      p[v] = u
      if rango[u] == rango[v]: rango[u] += 1

def kruskal(n, aristas):
   global p, rango
   p, rango = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
   for i in range(1, n + 1): makeSet(i)
   aristas.sort(key = lambda x: x[2])
   mst = 0
   for it in aristas:
      u, v, c = it
      if findSet(u) != findSet(v) or c < 0:
         unionSet(u, v)
         mst += c
   return mst

def dfs(visited, graph, node, act):
   if node in visited:
      if color[node-1] == color[act-1]:
         bipart.append(False)
   else:
      if color[node-1] == 0:
         color[node-1] = color[act-1]*(-1)
      visited.add(node)
      for i in range(len(graph[node-1])):
         dfs(visited, graph, graph[node-1][i], node)

def bipartito(adj):
   global color, bipart
   bipart = []
   color = [0 for _ in range(len(adj))]
   color[0] = 1
   visited = set()
   dfs(visited, adj, 1,1)
   return len(bipart) == 0

def main():
   N = int(stdin.readline())
   while N != 0:
      pairs = []
      adj = [[] for _ in range(N)]
      E = int(stdin.readline())
      for i in range(E):
         u, v, w = map(int, stdin.readline().split())
         pairs.append([u,v,w])
         adj[v-1].append(u)
         adj[u-1].append(v)
      bipar = bipartito(adj)
      if bipar:
         pairs.sort(key=lambda x: x[2])
         mst = kruskal(N, pairs)
         print(mst)
      else:
         print("Invalid data, Idiot!")
      N = int(stdin.readline())

main()