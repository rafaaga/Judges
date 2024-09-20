from sys import *

def binarySearch(x, y):
    low, hi = 1, y
    diff = y-x
    while(low + 1 != hi):
        mid = low + (hi - low) // 2
        slow = mid * diff
        if(slow >= y):
            hi = mid
        else:
            low = mid
    return hi

def main():
    line = stdin.readline()
    while(line):
        x,y = map(int, line.split())
        print(binarySearch(x,y))
        line = stdin.readline()
main()
