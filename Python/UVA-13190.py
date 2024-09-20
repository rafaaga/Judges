from sys import stdin
import heapq

def procedure(dose, frec, meds):
    for i in range(dose):
        actual = heapq.heappop(frec)
        mins, name = actual[0][0], actual[1]
        print(str(mins)+" "+name)
        heapq.heappush(frec, ((mins+meds.get(name), actual[0][1]), name))

def main():
    C = int(stdin.readline())
    for i in range(C):
        input = stdin.readline().split()
        num, dose = int(input[0]), int(input[1])
        frec, meds = [], {}
        for j in range(num):
            medsIn = stdin.readline().split()
            meds[medsIn[0]] = int(medsIn[1])
            heapq.heappush(frec, ((int(medsIn[1]), j), medsIn[0]))
        procedure(dose, frec, meds)

main()