from sys import *

def solveAsc(tian, king, n):
    ans = 0
    tian.sort(reverse=True)
    king.sort(reverse=True)
    lowTian, lowKing, hiTian, hiKing = 0, 0, n-1, n-1
    i, empate = 0, False
    while i < n and not empate:
        if tian[lowTian] > king[lowKing]:
            ans += 200
            lowTian += 1
            lowKing += 1
        elif tian[hiTian] > king[hiKing]:
            ans += 200
            hiKing -= 1
            hiTian -= 1
        elif tian[hiTian] < king[lowKing]:
            ans -= 200
            hiTian -= 1
            lowKing += 1
        else:
            empate = True
        i += 1
    return ans

def main():
    n = int(stdin.readline())
    while n != 0:
        tian = list(map(int, stdin.readline().split()))
        king = list(map(int, stdin.readline().split()))
        ans1 = solveAsc(tian, king, n)
        print(ans1)
        n = int(stdin.readline())

main()