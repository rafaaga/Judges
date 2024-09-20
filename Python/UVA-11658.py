from sys import *

def phi(n, porcentaje, mem):
    ans = None
    if (n, porcentaje) in mem: ans = mem[(n, porcentaje)]
    else:
        if n == len(p) and porcentaje <= 5000: ans = float('inf')
        elif porcentaje > 5000:
            ans = porcentaje
        else:
            ans = min(phi(n + 1, porcentaje, mem), (phi(n + 1, porcentaje + p[n], mem)))
        mem[(n,porcentaje)] = ans
    return ans


def main():
    global obj, p
    n, x = map(int, stdin.readline().split())
    while n != 0 or x != 0:
        p, mem = [], {}
        for i in range(n):
            val = float(stdin.readline())
            if i != x-1:
                p.append(int(round(val*100)))
            else:
                obj = int(round(val*100))
        if obj >= 5000:
            ans = 100
        else:
            ans = (obj/phi(0, obj, mem))*100
        print("{:.2f}".format(ans))
        n, x = map(int, stdin.readline().split()) 
main()