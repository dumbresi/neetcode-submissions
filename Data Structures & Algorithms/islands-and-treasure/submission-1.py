class Solution:

    def calculateDiSt(self,grid:List[List[int]],row: int, col:int)->None:
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        queue=deque()
        queue.append([row,col])
        dist=0
        while queue:
            # print(queue)
            dist+=1
            for i in range(len(queue)):
                rp,cp=queue.popleft()
                
                for d in directions:
                    r=rp+d[0]
                    c=cp+d[1]
                    if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]!=0 and grid[r][c]!=-1:
                        if(grid[r][c]>dist):
                            grid[r][c]=grid[rp][cp]+1
                            queue.append([r,c])



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    self.calculateDiSt(grid,i,j)


        