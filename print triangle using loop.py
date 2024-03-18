'''
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''

# Using for loop
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print the number
        print(rows - i, end=' ')
    # new line after each row
    print()

# Using while loop
row = int(input("Enter number of rows: "))
i = 0
while i < row:
    j = 0
    while j < i + 1:
        print(row - i, end=' ')
        j = j + 1
    i = i + 1
    print()
