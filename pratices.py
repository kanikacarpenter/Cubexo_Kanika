rows = 5 
for i in range(1, rows + 1):
    print("*" * i)

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i )+ "*" * i)

rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

    rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
