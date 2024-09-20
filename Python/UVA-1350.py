from sys import stdin

def search(A, x):
    ans, low, hi = None, 0, len(A)
    if low != hi:
        while low+1 != hi:
            mid = low + ((hi-low)>>1)
            if A[mid] <= x:
                low = mid
            else:
                hi = mid
        ans = low
    return ans

def process(fibo, num):
    ans = None
    base = search(fibo, num)
    dif = num - fibo[base]
    if dif == 0:
        ans = 1 * (10**(base))
    else:
        ans = 1 * (10**(base)) + process(fibo, dif)
    return ans

def fibonacci(x):
    secuencia = [1, 2]
    while secuencia[-1] <= x:
        siguiente_numero = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_numero)
    return secuencia[:-1]

def main():
    cases = int(stdin.readline())
    fibo = fibonacci(90000000)
    for _ in range(cases):
        num = int(stdin.readline())
        ans = process(fibo, num)
        print(ans)

main()