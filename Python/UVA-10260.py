from sys import *

def trad(cad):
    ans = None
    dic = {1:["B","F","P","V"],
           2:["C","G","J","K","Q","S","X","Z"],
           3:["D", "T"],
           4:["L"],
           5:["M","N"],
           6:["R"]}
    for i in range(1,len(dic)+1):
        if cad in dic[i]:
            ans = str(i)
    return ans

def main():
    line = stdin.readline()
    while line:
        cad = ""
        prevcad = None
        for i in range(len(line)):
            caracter = trad(line[i])
            if caracter != None and caracter != prevcad:
                cad += caracter
            prevcad = caracter
        print(cad)
        line = stdin.readline()

main()