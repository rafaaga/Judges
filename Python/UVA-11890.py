from sys import *

def solve(expression, a):
   a.sort()
   low, hi = 0, len(a)-1
   ans = 0
   pila = [1]
   for i in range(len(expression)):
      if(expression[i] == "x"):
         if expression[i-1] == "-":
            if pila[-1] == 1:
               ans -= a[low]
               low += 1
            elif pila[-1] == -1:
               ans += a[hi]
               hi -= 1
         else:
            if pila[-1] == 1:
               ans += a[hi]
               hi -= 1
            elif pila[-1] == -1:
               ans -= a[low]
               low += 1
      elif(expression[i]=="("):
         if i > 0 and expression[i-1] == "-":
            pila.append(pila[-1]*(-1))
         else:
            pila.append(pila[-1])
      elif(expression[i]==")"):
         pila.pop()
   return ans

def main():
    T = int(stdin.readline())
    for _ in range(T):
        expression = stdin.readline()
        N = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        res = solve(expression, a)
        print(res)
main()