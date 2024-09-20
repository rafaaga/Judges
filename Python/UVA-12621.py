from sys import *

def solve(n, cal, courses, mem):
    ans = None
    if (n, cal) in mem: ans = mem[(n, cal)]
    else:
        if n == 0 and cal > 0: ans = 250000
        elif cal <= 0:
            ans = 0
        else:
            ans = min(solve(n - 1, cal, courses, mem), solve(n - 1, cal - (courses[n - 1]), courses, mem) + courses[n - 1])
        mem[(n,cal)] = ans
    return ans

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        mem = {}
        calmin = int(stdin.readline())
        p = int(stdin.readline())
        courses = list(map(int, stdin.readline().split()))
        res = solve(p, calmin, courses, mem)
        if res == 250000:
            print("NO SOLUTION")
        else:
            print(f"{res}")
main()