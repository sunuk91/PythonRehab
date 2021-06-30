#Back Tracking Algorithm
#Map Question
import sys

sys.setrecursionlimit(10000)

# map = [[0,1,1,1],[0,0,1,0],[1,0,1,1],[0,0,0,0]]
map = [[0,0,0],[0,1,0],[0,0,0]]
map_size = [len(map), len(map[0])]
visited =[[0,0,0],[0,0,0],[0,0,0]]

dx = [1,0]
dy = [0,1]

output = []
root = []

start = [0,0]
end = [map_size[0]-1,map_size[1]-1]

def isSafe(x,y):
    if x>=0 and x<map_size[0] and y>=0 and y<map_size[1] and map[x][y]==0: return True
    return False

# def isVisited(x,y,visited):
#     if visited[x][y]==1: return True
#     return False

# def find_way(a,b):
#     if a == end[0] and b == end[1]:
#         # print(visited)
#         print('success')
#     else:
#         for t in range(4):
#             if not isSafe(a + dy[t], b + dx[t]):
#                 # print(a + dy[t], b + dx[t])
#                 continue
#             else:
#                 # print('hi')
#                 if ~isVisited(a + dy[t], b + dx[t], visited):
#                     print(visited)
#                     visited[a + dy[t]][b + dx[t]] = 1
#                     find_way(a + dy[t], b + dx[t])

path = []
def find_way(a,b):
    if a == end[0] and b == end[1]:
        print('success')
        path.append([a,b])
        return True
    if isSafe(a,b):
        path.append([a,b])
        if find_way(a+dy[0], b+dx[0]): return True
        if find_way(a + dy[1], b + dx[1]): return True
    else:
        # print(a, b)
        return False


result = find_way(0,0)
print(result)
print(path)
# print(~True)
# print(map_size)
# print(map_size[0]+map_size[1])