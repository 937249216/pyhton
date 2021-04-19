class Solution:
    def solveNQueens(self, n: int):
        self.res = []
        trans = lambda path: ['.'*i + 'Q' + '.'*(len(path)-1-i) for i in path]
        def recursion(path, pos):
            if len(path) == n:
                self.res.append(trans(path))
                return
                l , r = pos
                l , r = [i-1 for i in l], [i+1 for i in r]
                total = l+r+path
                for cand in range(n):
                    if cand in total:
                        continue
                    recursion(path+[cand], [l+[cand], r+[cand]])
        
        recursion([], [[], []])
        return self.res
a=Solution.solveNQueens  
      
print(a(8))
