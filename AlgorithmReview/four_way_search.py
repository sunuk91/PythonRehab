
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def get_four_ways(input:list, i, j):

    result = []
    for t in range(4):
        ny = j + dy[t]
        nx = i + dx[t]
        result.append(input[ny][nx])
    return result


input = [[1,2,3],[4,5,6],[7,8,9]]

print(get_four_ways(input, 1,1))



