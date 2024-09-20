from sys import *
from math import *

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

def kruskal(n, sensors, rt, aristas):
    global p, rango
    p, rango = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
    for i in range(1, n + 1): makeSet(i)
    aristas.sort(key = lambda x: x[2])
    mst = []
    i = 0
    while i < n and len(mst) < (sensors-rt):
        u, v, c = aristas[i][0], aristas[i][1], aristas[i][2]
        if findSet(u) != findSet(v):
            unionSet(u, v)
            mst.append(c)
        i += 1
    return mst[-1]

def calcularDistancias(sensors):
    ans = []
    for i in range(len(sensors)):
        for j in range(i+1, len(sensors)):
            A, B = sensors[i], sensors[j]
            x, y = (B[0]-A[0]), (B[1]-A[1])
            dist = sqrt(((x*x)+(y*y)))
            ans.append([i, j, ceil(dist)])
    return ans

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        rt = int(stdin.readline())
        coordinates = stdin.readline().split()
        sensors = []
        while len(coordinates) > 1:
            X, Y = map(int, coordinates)
            sensors.append((X,Y))
            coordinates = stdin.readline().split()
        distancias = calcularDistancias(sensors)
        ans = kruskal(len(distancias), len(sensors), rt, distancias)
        print(ans)

main()