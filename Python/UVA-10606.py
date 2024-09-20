from sys import *

def search(x):
    left, right = 1, x+1
    while left + 1 != right:
        mid = left + ((right-left)>>1) 
        if mid * mid <= x:
            left = mid
        else:
            right = mid
    return left * left

def main():
    line = int(stdin.readline())
    while line != 0:
        ans = search(line)
        print(ans)
        line = int(stdin.readline())

main()