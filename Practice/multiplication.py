# Size of the table
size = 20

# Header row
print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:5}", end="")
print("\n" + "-" * (size * 5 + 5))

# Rows
for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, size + 1):
        print(f"{i * j:5}", end="")
    print()
