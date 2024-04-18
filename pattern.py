row = int(input("enter the number of rows:"))
column = int(input("enter the number of columns:"))
symbol = input("symbol")

for i in range(row):
    for j in range(column):
        print(symbol, end="")
    print()    