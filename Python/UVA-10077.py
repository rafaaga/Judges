from sys import stdin

def solve(m, n):
    cad = []
    mp, np = 1, 1 
    parents = [(0,1), (1,0)]
    while m != mp or n != np:
            if m*np < mp*n:
                parents = [parents[0], (mp, np)]
                mp, np = parents[0][0]+parents[1][0], parents[0][1]+parents[1][1]
                cad.append("L")
            else:
                parents = [(mp, np), parents[1]]
                mp, np = parents[0][0]+parents[1][0], parents[0][1]+parents[1][1]
                cad.append("R")
    return cad

def main():
    m, n = map(int, stdin.readline().split())
    while m!= 1 or n!=1:
        cad = solve(m,n)
        cad = ''.join(cad)
        print(cad)
        m, n = map(int, stdin.readline().split())

main()