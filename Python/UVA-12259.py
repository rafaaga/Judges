from sys import *

def solve(A, index, p, n):
   ans = [0 for _ in range(n)]
   for i in range(len(A)):
      cuota = p//n
      if cuota > A[index[i]]:
         ans[index[i]] = A[index[i]]
      else:
         ans[index[i]] = cuota
      p -= ans[index[i]]
      n -= 1
   return ans

def main():
   casos = int(stdin.readline())
   for _ in range(casos):
      aux, A = {}, []
      p, n = map(int, stdin.readline().split())
      cents = list(map(int, stdin.readline().split()))
      for i in range(n):
         if cents[i] not in aux:
            aux[cents[i]] = [i]
         else:
            aux[cents[i]].append(i)
      aux = dict(sorted(aux.items()))
      for i in aux:
         l = aux.get(i)
         for j in range(len(l)-1,-1,-1):
            A.append(l[j])
      ans = solve(cents, A, p, n)
      final = sum(ans)
      if final < p:
         print("IMPOSSIBLE")
      else:
         for i in range(len(ans)-1):
            print(f"{ans[i]}", end=" ")
         print(f"{ans[-1]}")
main()