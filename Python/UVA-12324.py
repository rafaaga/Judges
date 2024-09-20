from sys import *

def phi(n, e, T, E, mem):
    ans = None
    if (n, e) in mem: ans = mem[(n, e)]
    else:
        if n == len(T): ans = 0
        elif e >= len(T)-n:
            ans = T[n]//2 + phi(n+1, e + E[n]-1, T, E, mem)
        elif n != len(T) and e == 0:
            ans = T[n] + phi(n+1, E[n], T, E, mem)
        else:
            ans = min(T[n] + phi(n+1, e+E[n], T, E, mem), T[n]//2 + phi(n+1, e + E[n]-1, T, E, mem))
        mem[(n,e)] = ans
    return ans

def main():
    travels = int(stdin.readline())
    while travels != 0:
        T, E, mem = [], [], {}
        for _ in range(travels):
            t, e = map(int, stdin.readline().split())
            T.append(t)
            E.append(e)
        ans = phi(0, 0, T, E, mem)
        print(ans)
        travels = int(stdin.readline())
main()