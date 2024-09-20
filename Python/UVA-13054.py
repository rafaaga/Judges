from sys import stdin

def procedure(hippos, n, h, Ta, Td):
    hippos.sort()
    time, p_init, p_end = 0, 0, (n-1)
    while p_init <= p_end:
        if(hippos[p_init] + hippos[p_end]) < h and Td <= (2*Ta) and p_init!=p_end:
            time += Td
            p_init += 1
            p_end -= 1
        else:                
            p_end -= 1
            time += Ta
    return time

def main():
    C = int(stdin.readline())
    for i in range(C):
        input = stdin.readline().split()
        n, h, Ta, Td = int(input[0]), int(input[1]), int(input[2]), int(input[3])
        hippos = list(map(int,stdin.readline().split())) 
        time = procedure(hippos, n, h, Ta, Td)
        print(f"Case {i+1}: {time}")
main()