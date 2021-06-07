class solution:
    def slove(self,n:int):
        def generateboard():
            board = list()
            for i in range(n):
                row[queens[i]] = "q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board    

        def backtrack(row: int):
            if row == n :
                board = generateboard()
                solution.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row +i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    colimns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
'''

class Solution:
     def solveNQueens(self, n: int) -> list[list[str]]:
        self.res = []
        trans = lambda path:['.'*i+'Q'+'.'*(len(path)-1-i)for i in path]
        def  recursion(n,path,pos):
            if len(path) == n:
                self.res.append(trans(path))
                return
            l,r,m = pos
            l,r =[i-1 for i in l],[i+1 for i in r]
            total = l+r+m
            for cand in range(n):
                if cand in total:
                    continue
                recursion(n,path+[cand],[l+[cand],r+[cand],m+[cand]])

        recursion(n,[],[[],[]])
        return self.res
     '''