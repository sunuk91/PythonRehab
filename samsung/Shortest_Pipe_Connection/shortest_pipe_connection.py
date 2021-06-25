import os
# 상하, 좌우
# -1+1,-1+1

script_dir = os.path.dirname(__file__)
f = open(os.path.join(script_dir, 'sample_sample_input.txt'), 'r')

num_tc = int(f.readline())
tc = {}
for i in range(num_tc):
    lines = int(f.readline())
    sub_tc = []
    for _ in range(lines):
        sub_tc.append(f.readline().split(' ')[:-1])
    tc[i] = sub_tc
f.close()

print(tc)

type = {
    0: {},
    1: {
        0: [[0,-1], [0,1]],
        1: [[-1,0], [1,0]]
    },
    2: {
        0: [[-1,0], [1, 0]],
        1: [[0,-1],[0,1]]
    },
    3: {
        0: [[1,0], [0,1]],
        1: [[1,0],[0,-1]],
        2: [[0,-1],[-1,0]],
        3: [[-1,0],[0,1]]
    },
    4: {
        0: [[0,-1], [1,0]],
        1: [[0,-1],[-1,0]],
        2: [[-1,0],[0,1]],
        3: [[0,1],[1,0]],
    },
    5: {
        0: [[0,-1],[-1,0]],
        1: [[-1,0],[0,1]],
        2: [[0,1],[1,0]],
        3: [[1,0],[0,-1]],
    },
    6: {
        0: [[-1,0],[0,1]],
        1: [[0,1], [1,0]],
        2: [[1,0],[0,-1]],
        3: [[0,-1], [-1,0]]
    }
}


