from sys import *

def solve(songs, N, S):
    ans = 0
    l = []
    for i in range(N):
        val = songs[i][1]/songs[i][2]
        l.append([val, songs[i][0]])
    l.sort()
    ans = l[S-1][1]
    return int(ans)

def main():
    line = stdin.readline()
    while line:
        N = int(line)
        songs = []
        while len(songs) < N:
            data = list(map(float, stdin.readline().split()))
            for i in range(0, len(data)-1, 3):
                songs.append([data[i], data[i+1], data[i+2]])
        S = int(stdin.readline())
        ans = solve(songs, N, S)
        print(ans)
        line = stdin.readline()

main()