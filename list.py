# Matrix arithmatics

x = [[11,33,55], [21,3,6],[7, 11,10]]

y = [[23,20,11],[34,21,9], [10,22,34]]
# print(len(x))
# print(x[1])
z = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] + y[i][j]

for i in z:
    print(i)