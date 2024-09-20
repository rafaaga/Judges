from math import *
from sys import *

def f(T, x):
    return (T*3600*24*x)

def biseccion(f, T, a, b, v):
    low, hi, ans = a, b, None
    eps = 1e-6
    it = 0
    while hi - low > eps:
        mid = (hi + low) / 2
        if v <= f(T,mid): hi = mid
        else: low = mid
        it += 1
    ans = low
    return ans

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        input = stdin.readline().split()
        T, S, D = int(input[0]), int(input[1]), int(input[2])
        mass_change = biseccion(f, T, -1000000, 1000000, (D*1000000))
        if mass_change > 0: mass_change = floor(mass_change)
        else: mass_change = ceil(mass_change)
        if mass_change > 0:
            print(f"Remove {mass_change} tons")
        elif mass_change < 0:
            print(f"Add {abs(mass_change)} tons")
        else:
            print("Add 0 tons")

main()