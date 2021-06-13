import numpy as np

# https://www.acmicpc.net/problem/1012

ax = np.zeros((10,10))
fill = [[0,0], [1,0], [1,1], [4,2], [4,3], [4,5], [2, 4], [3,4], [7,4], [8,4], [9,4], [7,5], [8,5]]
for i in fill:
    ax[i[0]][i[1]] = 1


visited = [[0]*50]*50

# dy = (-1, 0, 1, 0)
# dx = (0, 1, 0, -1)
#
# def dfs(y, x):
#     visited[y][x] = 1;
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dy[i]
#         if(ny<0 or nx<0 or ny>n or nx>m): continue
#         if()

# test = [[1,2,3], [4,5,6]]
# test[1][2] =0
# print(test)
# ax[0][1] = 50
# print(ax)
