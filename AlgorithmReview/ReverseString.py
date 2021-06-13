
def reverseStr(my_str : str):
    reversed = ''
    for c in range(len(my_str)):
        reversed = reversed + my_str[len(my_str) - c - 1]
    return reversed

def reverse_list_of_string(my_str: str):
    str_by_word = my_str.split()
    result = []
    for idx in range(len(str_by_word)):
        result.append(reverseStr(str_by_word[len(str_by_word)-idx-1]))
    return result

my_str = 'abcdefghi'
my_str_list = "My Name is SunUk Kim"

print(reverseStr(my_str))
print(reverse_list_of_string(my_str_list))