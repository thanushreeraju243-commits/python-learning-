rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))   
symbol = input("Enter the symbol to fill the matrix: ")
for i in range(rows):
    for j in range(cols):
        print(symbol, end=' ')
    print()
    