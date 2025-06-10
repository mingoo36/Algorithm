import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


    


for _ in range(int(input())):
    m,n,k = map(int,input().split())

    graph = [[0]*m for _ in range(n)]  

    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    def dfs(x,y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        
        if graph[x][y] == 1:
            graph[x][y] = 0

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return True
        return False
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                result += 1
    print(result)

 