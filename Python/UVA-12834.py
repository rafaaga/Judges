from sys import *

def solve(X, Y, k):
    proffit = []
    for i in range(len(X)):
        proffit.append(Y[i]-X[i])
    proffit.sort()
    for i in range(k):
        if proffit[i] < 0:
            proffit[i] = 0
    return sum(proffit)

def main():
    T = int(stdin.readline())
    for i in range(T):
        n, k = map(int, stdin.readline().split())
        X = list(map(int, stdin.readline().split()))
        Y = list(map(int, stdin.readline().split()))
        ans = solve(X, Y, k)
        if ans > 0:
            print(f"Case {i+1}: {ans}")
        else:
           print(f"Case {i+1}: No Profit") 
main()