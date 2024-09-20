from sys import stdin

def createSet(p, ran, sums, ident, val):
   p.append(val)
   ran.append(1)
   sums.append([1, val])
   ident[val] = val
   return p, ran, sums, ident

def findSet(p, num):
   if p[num-1] != num:
      p[num-1] = findSet(p, p[num-1])
   return p[num-1]

def unionSets(p, ran, sums, ident, set1, set2):
   set1, set2 = ident[set1], ident[set2]
   xroot, yroot = findSet(p, set1), findSet(p, set2)
   if xroot != yroot:
      if ran[xroot-1] > ran[yroot-1]:
         p[yroot-1] = xroot
         sums[xroot-1][0] += sums[yroot-1][0]
         sums[xroot-1][1] += sums[yroot-1][1]
      else:
         sums[yroot-1][0] += sums[xroot-1][0]
         sums[yroot-1][1] += sums[xroot-1][1]
         p[xroot-1] = yroot
         if ran[xroot-1] == ran[yroot-1]:
            ran[yroot-1] += 1
   return p, ran, sums, ident

def changeSets(p, ran, sums, ident, set1, set2):
   orset = set1
   set1, set2 = ident[set1], ident[set2]
   xroot, yroot = findSet(p, set1), findSet(p, set2)
   if xroot != yroot:
      if ran[set1-1] == 1 and xroot == set1:
         unionSets(p, ran, sums, ident, set1, set2)
      elif ran[set1-1] == 1 and xroot != set1:
         sums[xroot-1][0] -=1
         sums[xroot-1][1] -= orset
         p[set1-1] = set1
         unionSets(p, ran, sums, ident, set1, set2)
      else:
         sums[xroot-1][0] -= 1
         sums[xroot-1][1] -= orset
         new = len(p)+1
         p, ran, sums, ident = createSet(p, ran, sums, ident, new)
         ident[set1] = new
         sums[new-1] = [1, orset]
         unionSets(p, ran, sums, ident, set1, set2)
   return p, ran, sums, ident

def sumAccum(p, sums, ident, num):
   num = ident[num]
   num = findSet(p,  num)
   print(str(sums[num-1][0]) + " " + str(sums[num-1][1]))

def main():
   line = stdin.readline().split()
   while line:
      p, ran, sums, ident = [], [], [], {}
      n, m = int(line[0]), int(line[1])
      for i in range(1, n+1):
         p, ran, sums, ident = createSet(p, ran, sums, ident, i)
      for i in range(m):
         op = stdin.readline().split()
         if int(op[0]) == 1:
           p, ran, sums, ident = unionSets(p, ran, sums, ident, int(op[1]), int(op[2]))
         elif int(op[0]) == 2:
            p, ran, sums, ident = changeSets(p, ran, sums, ident, int(op[1]), int(op[2]))
         elif int(op[0]) == 3:
            sumAccum(p, sums, ident, int(op[1]))
      line = stdin.readline().split()
      
main()