from sys import *

def solve(line):
    abcdario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters, freq = "", 0
    dic = {}
    for i in range(len(line)):
        if line[i] in abcdario:
            if line[i] not in dic:
                dic[line[i]] = 1
            else:
                dic[line[i]] += 1
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: (-item[1], item[0]))}
    freq = max(dic.values())
    for k, v in dic.items():
        if v != freq:
            break
        letters += k
        
    return letters, freq

def main():
    line = stdin.readline()
    while line:
        l, f = solve(line)
        print(f"{l} {f}")
        line = stdin.readline()

main()