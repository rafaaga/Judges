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
    mst = []
    i = len(aristas)-1
    while i > -1 and len(mst) < n-1:
            u, v = aristas[i][1], aristas[i][2]
            a1 = findSet(u)
            a2 = findSet(v)
            if a1 != a2:
                mst.append(aristas[i][0])
                unionSet(u, v)
            i -= 1
    return mst if len(mst) >= n-1 else []

def solve(G, n):
    ans = 100000000
    while len(G) >= n-1:
        mst = kruskal(n, G)
        if len(mst) != 0:
            diff = mst[-1]-mst[0]
            if(diff) < ans:
                ans = diff
        G.pop()
    return ans

def main():
    n, m = map(int, stdin.readline().split())
    while n != 0 or m != 0:
        G = []
        for i in range(m):
            u, v, w = map(int, stdin.readline().split())
            G.append([w,u,v])
        if m >= n-1:
            G.sort(reverse=True)
            ans = solve(G, n)
            if(ans == 100000000):
                print(-1)
            else:
                print(ans)
        else:
            print(-1)
        n, m = map(int, stdin.readline().split())
main()