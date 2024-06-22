'''def convert_case(input_string):
    converted_string = ""
    for char in input_string:
        if char.islower():
            converted_string += char.upper()
        elif char.isupper():
            converted_string += char.lower()
        else:
            converted_string += char
    return converted_string

# Example usage:
input_string = "Hello World"
converted_string = convert_case(input_string)
print("Original:", input_string)
print("Converted:", converted_string)
'''
def generate_all_binary_strings(n, arr, i):
    if i == n:
        print(*arr)
        return
    arr[i] = 0
    generate_all_binary_strings(n, arr, i + 1)
    arr[i] = 1
    generate_all_binary_strings(n, arr, i + 1)

# Example usage:
n = 4
arr = [0] * n
generate_all_binary_strings(n, arr, 0)