from sys import stdin

def move(r, c, N):
   ans = []
   if r >= N:
      ans = [c, c+1]
   else:
      if c!=0: ans.append(c-1)
      if c!=r: ans.append(c)
   return ans

def phi(r, c, x, N, board, mem):
   ans = False
   if (r, c, x) in mem: ans = mem[(r, c, x)]
   else:
      if r==0:
         ans = abs(board[0][0]) == x
      else:
         n, row = 0, move(r, c, N)
         while not ans and n != len(row):
            ans = phi(r-1, row[n], x+board[r][c], N, board, mem) or phi(r-1, row[n], x-board[r][c], N, board, mem)
            n += 1
      mem[(r, c, x)] = ans
   return ans

def main():
   ans = None
   N = int(stdin.readline())
   while N != 0:
      board, mem, found = [], {}, False
      rows, n = (N*2)-1, 0
      for _ in range(rows):
         board.append(list(map(int, stdin.readline().split())))
      while not found:
         found = phi(rows-1, 0, n, N, board, mem) or phi(rows-1, 0, -n, N, board, mem)
         if found:
            ans = n
         n += 1
      print(ans)
      N = int(stdin.readline())

main()