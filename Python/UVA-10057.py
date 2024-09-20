from sys import stdin

def searchFirst(l, left, right, x):
    ans, found = right, False
    while left < right:
        mid = left + ((right - left) >> 1)
        if l[mid] == x and (mid == 0 or l[mid-1] < x):
            ans, found = mid, True
            right = mid
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid
    if not found:
        ans = -1
    return ans

def searchLast(l, left, right, x):
    ans, found = right, False
    while left < right:
        mid = left + ((right - left) >> 1)
        if l[mid] == x:
            ans, found = mid, True
            left = mid + 1
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid
    if not found:
        ans = - 1
    return ans


def process(l):
    l.sort()
    left, right = 0, len(l)-1
    med1, med2 = right>>1, right>>1
    if len(l) % 2 == 0: med2 = (right>>1) + 1
    numA = (l[med2] - l[med1]) + 1
    a = (med1 - searchFirst(l, 0, med1+1, l[med1])) + 1
    if len(l) % 2 == 0:
        b = (searchLast(l, med2, len(l), l[med2]) - med2) +1
    else:
        b = searchLast(l, med2, len(l), l[med2]) - (med2+1) +1
    return l[med1], (a+b), numA

def main():
    line = stdin.readline().split()
    while line:
        l = []
        for _ in range(int(line[0])):
            l.append(int(stdin.readline()))
        a, b, c = process(l)
        print(f"{a} {b} {c}")
        line = stdin.readline().split()
main()