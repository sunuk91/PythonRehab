
dict = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

output = []
input = '94523'

def BT(index, letter):
    if index >= len(input):
        output.append(letter)
    else:
        num = input[index]
        cbars = dict[num]
        # print(index, len(input))
        for c in cbars:
            BT(index+1, letter+c)


BT(0,'')
print(output, len(output))