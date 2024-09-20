from sys import *

def solve(l1, l2):
    ans = 0
    cads = set()
    for i in range(len(l1)):
        for j in range(len(l2)):
            cad = l1[i]+l2[j]
            new_string = cad.replace('\n', '')
            cads.add(new_string)
    ans = len(cads)
    return ans

def main():
    casos = int(stdin.readline())
    for i in range(casos):
        M, N = map(int, stdin.readline().split())
        l1, l2 = [], []
        for j in range(M):
            l1.append(stdin.readline())
        for j in range(N):
            l2.append(stdin.readline())
        ans = solve(l1,l2)
        print(f"Case {i+1}: {ans}")
main()