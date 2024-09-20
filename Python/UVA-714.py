from sys import stdin

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


def solve(books, k):
    l, r = max(books), sum(books)
    while l < r:
        mid = l + ((r-l)>>1)
        if f(mid, k, books) <= k:
            r = mid
        else:
            l = mid + 1
    return l

def main():
    N = int(stdin.readline())
    for _ in range(N):
        m, k = map(int, stdin.readline().split())
        books = list(map(int, stdin.readline().split()))
        maxCap = solve(books, k)
        cad = []
        acum, count = 0, 0
        for i in range(len(books)-1, -1, -1):
            if acum + books[i] <= maxCap:
                cad.append(books[i])
                acum += books[i]
            elif i == 0 and count == k:
                cad.append(books[0])
            else:
                cad.append("/")
                cad.append(books[i])
                acum = books[i]
                count += 1
        for i in range(len(cad)-1, 0, -1):
            if i > 0 and count < k-1 and cad[i] != '/' and cad[i-1]!= '/':
                print(f"{cad[i]}", end=" / ")
                count += 1
            else:
                print(f"{cad[i]}", end=" ")
        print(f"{cad[0]}")

main()