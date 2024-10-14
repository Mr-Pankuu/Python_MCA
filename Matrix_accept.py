m = [[], [], [], [], [], [], []]

r = int(input("Enter the ro value: "))
c = int(input("Enter the column value: "))

for i in range(r):
    for j in range(c):
        m[i].append(int(input(f"Enter element at {i},{j}: ")))

for i in range(m):
    print(m[i])