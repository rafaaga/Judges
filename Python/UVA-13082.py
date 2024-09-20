from sys import *

def solve(heights):
    ans = len(heights)
    act = 0
    sortedHeights = heights.copy()
    sortedHeights.sort()
    for i in range(len(heights)):
        if heights[i] == sortedHeights[act]:
            ans -= 1
            act += 1
    return ans 

def main():
    T = int(stdin.readline())
    for i in range(T):
        n = int(stdin.readline())
        heights = list(map(int, stdin.readline().split()))
        ans = solve(heights)
        print(f"Case {i+1}: {ans}")

main()