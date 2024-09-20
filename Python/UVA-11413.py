from sys import *

def f(x, k, A):
    ans, ac, i = 1, 0, 0
    while i < len(A) and ans <= k:
        if ac + A[i] <= x:
         ac += A[i]
        else:
            ans += 1
            ac = A[i]
        i += 1
    return ans

def solve(A, k):
    l, r = max(A), sum(A)
    while l < r:
        mid = l + ((r-l)>>1)
        if f(mid, k, A) <= k:
            r = mid
        else:
            l = mid + 1
    return l

def main():
   line = stdin.readline()
   while line:
      n, m = map(int, line.split())
      A = list(map(int, stdin.readline().split()))
      print(solve(A, m))
      line = stdin.readline()
main()