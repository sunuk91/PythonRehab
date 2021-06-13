
# https://www.acmicpc.net/problem/11659


def cum_sum(input: list):
    cum = [input[0]]
    for i in range(1, len(input)):
        cum.append(cum[i-1]+ input[i])
    return cum

def idx_sum(cum_sum: list ,i,j):
    return cum_sum[j] - cum_sum[i-1]


input = [1,2,3,4,5,6,7]
cs = cum_sum(input)
print(idx_sum(cs, 5, 5))
print(idx_sum(cs, 2, 4))