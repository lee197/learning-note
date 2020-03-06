# 概念：

# 图由边跟点组成，可以运用在各种复杂关系的标示，比如电路中各元件之间关系，高速公路网，航线交通，因特网，局域网等等

# 三种标示形式：邻接矩阵，邻接列表，点线集合

# 点线集合：

# [ [0,1], [0,6], [0,8], [1,4], [1,6], [1,9], [2,4], [2,6], [3,4], [3,5],
# [3,8], [4,5], [4,9], [7,8], [7,9] ]
# 邻接矩阵：

# [ [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
#   [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
#   [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
#   [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#   [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#   [0, 1, 0, 0, 1, 0, 0, 1, 0, 0] ]
# 邻接列表：

# [ [1, 6, 8],
#   [0, 4, 6, 9],
#   [4, 6],
#   [4, 5, 8],
#   [1, 2, 3, 5, 9],
#   [3, 4],
#   [0, 1, 2],
#   [8, 9],
#   [0, 3, 7],
#   [1, 4, 7] ]
# 或：

# {1:[1, 6, 8],
#   2:[0, 4, 6, 9],
#   3:[4, 6],
#   4:[4, 5, 8],
#   5:[1, 2, 3, 5, 9],
#   6:[3, 4],
#   7:[0, 1, 2],
#   8:[8, 9],
#   9:[0, 3, 7],
#   0:[1, 4, 7]}
# 一般将邻接集合转换成邻接列表：

# graph = collections.defaultdict(list)
#         for edge in prerequisites:
#             graph[edge[0]].append([edge[1]])
# 在具体语言中有具体的表现形式：python中可以用dict[list]标示，key表示当前访问点，value是一个list表示其其邻接数组

# 重点掌握深度优先搜索（DFS）与广度优先搜索（BFS）

# 时间复杂度为O(|V|+|E|): V是顶点数，E是边数

# DFS：可用STACK来遍历，沿着一条路径走下去

# BFS：可用QUEUE来遍历，可从起点开始根据链接的每一层，层层遍历

# DFS与BFS对比：

# DFS占内存要少很多，BFS会在队列中存放每一层的多个节点，包括很多被访问过的节点

# 如果要查找的数据在树中较深，适合用DFS，如果要找的数据比较浅，就可以用BFS

# 实现代码：

# DFS:

class Graph:
   def __int__(self):

      self.graph = defaultdict(list) // 这个是用字典的形式来标示图key是顶点，value是数组，包含这个顶点的所有邻接点

   def addEdge(self,u,v):
      self.graph[u].append[v]

   def dfs(self):
      V = len(self.graph)         //整个字典的长度就是顶点数
      visited = [False]*(V)       // 创建一个数组全都是False，数量与顶点数相同，序号表示顶点值，值表示是否已经访问过
      for i in range(V):
        if visited[i] = False:    // 如果顶点被访问过就跳过
           self.dfsUtil(i,visited)
           
   def dfsUtil(self,v,visited):
       visited[v] = True
       print v
       for i in graph[v]:         // 如果这个graph[v]是空数组，就表示这个顶点到头了，可以向上返回
          if visited[i] == False: 
             self.dfsUtil(i,visited)  // 如果顶点没有访问过就一级一级递归
# BFS:

# 主要处理点的数据结构：QUEUE

# 其他：全局数组记录点是否已经被访问过了

# 进队列的时候更改全局访问数组为1，出队列的时候打印处理数据，查找其子节点

# 具体算法：进队列的前看看是否在visited中

#                   在的话就不进，不在的话就进队列

#                    出队列了再把元素加到visited当中

#                    注意：visited有多种数据格式，具体看需求，可以是key-value，可以是数组等等

class Graph:

   def __init__(self):
       self.graph = defaultdict[list]
   def addEdge(u,v):
       self,graph[u].append(v)
   def bfs(self,s):
       visited = [False]*(len(self.graph))
       queue=[]
       queue.append(s)
       visited[s] = true

       while queue:
             s = queue.pop(0)
             print s
             for i in self.graph[i]:
                 if visited[i] == False:
                    queue.push(i)
                    visited[i] = True
             
    class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue=collections.deque([node])
        head=Node(node.val,[])
        visited={node:head}

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in visited:
                    visited[node].neighbors.append(visited[neighbor])
                else:
                    queue.append(neighbor)
                    copy=Node(neighbor.val,[])
                    visited[neighbor]=copy
                    visited[node].neighbors.append(copy)
                        
                    
        return head
# 示例：问题一般都是是一些实际生活中的问题，要想办法将其转换成图的计算问题，比如这个问题：number of islands

class Solution:
  def numIslands(self, grid):
    def sinkIsland(grid, r, c):
      if grid[r][c] == '1':
        grid[r][c] = '0'
      else:
        return
      if r + 1 < len(grid):
        sinkIsland(grid, r + 1, c)
      if r - 1 >= 0:
        sinkIsland(grid, r - 1, c)
      if c + 1 < len(grid[0]):
        sinkIsland(grid, r, c + 1)
      if c - 1 >= 0:
        sinkIsland(grid, r, c - 1)
    counter = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          counter += 1
          sinkIsland(grid, i, j)
    return counter
  def findNeighbour(sr,sc,grid):
    rowLen = len(grid)
    colLen = len(grid[0])
    res = []

    if sr-1 >= 0 and sc < colLen and grid[sr-1][sc] == 1:
      res.append((sr-1,sc))

    if sr < rowLen and sc-1 >= 0 and grid[sr][sc-1] == 1:
      res.append((sr,sc-1))

    if sr+1 < rowLen and sc < colLen and grid[sr+1][sc] == 1:
      res.append((sr+1,sc)) 

    if sr < rowLen and sc+1 < colLen and grid[sr][sc+1] == 1:
      res.append((sr,sc+1)) 

    return resp
# 读题很容易知道这个关于图的问题，由于这是一个二维矩阵，所以要先考虑二维矩阵的遍历，在处理这个问题的时候我先考虑了把相关数据转化成图的结构然后再进行遍历，其实这是没有必要的

# 两个for循环：

    for i in range(len(grid)):
      for j in range(len(grid[0])):

    for row in gird:
       for column in row:

    在矩阵中遍历的时候，可以先提取矩阵信息：
      n = len(grid)
      m = len(len(grid[0])
      for i in range(m):
         for j in range(n):
    
    设定好搜索方向：
    self.directions = [(1,0),(-1,0),(0,1),(0,-1)]

    visited[i][j] = True
    for dir in self.directions:
        x, y = i + dir[0], j + dir[1]
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]：
                continue



# 就可以遍历矩阵，然后每当碰到目标点的时候就开始DFS，并计算counter

# dfs搜素示例：

 def dfs(self, matrix, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point 
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)
            
# 在矩阵中做二分查找：

 def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False