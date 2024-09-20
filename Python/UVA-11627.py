from sys import *

N, S = 100100, 1001000
gateX, gateY, skis = [None for _ in range(N)], [None for _ in range(N)], None
w, vh, n, s = int(), int(), int(), int()

def check(vs):
    flag, i = True, 1
    cla= gateX[0]
    cra = cla + w
    while i < n and flag:
        t = (gateY[i] - gateY[i - 1]) * 1.0 / vs
        cln = gateX[i]
        crn = cln + w
        cla = max(cla - t * vh, cln)
        cra = min(cra + t * vh, crn)
        if cla > cra: flag = False
        i += 1
    return flag

def solve():
    global s, gateX, gateY, skis, w, vh, n
    w, vh, n = map(int, stdin.readline().split())
    for i in range(n):
        gateX[i], gateY[i] = map(int, stdin.readline().split())
    s = int(stdin.readline())
    skis = []
    for i in range(s):
        skis.append(int(stdin.readline()))
    skis.sort()
    l, r = 0, s-1
    while l <= r:
        mid = (l + r) >>1
        if check(skis[mid]): l = mid + 1
        else: r = mid - 1
    if r < 0: print("IMPOSSIBLE")
    else: print("%d" % skis[r])

def main():
    case = 1
    t = int(stdin.readline())
    while t > 0:
        solve()
        t-= 1

main()