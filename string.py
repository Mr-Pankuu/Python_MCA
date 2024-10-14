list = ["HH", "EE", "MM", "PP", "QQ"]

# Create the half pyramid

# for i in range(0,len(list),1):
# #    print(list[i])
#     print()
#     for j in range(0,i+1,1):
#         print(list[i], end=" ")
#  Triangle 
for i in range(0,len(list),1):
#    print(list[i])
    print()
    for j in range(0,i+1,1):
        print(list[i], end=" ")
for i in range(len(list)-2,-1,-1):
    print()
    for j in range(0,i+1,1):
        print(list[i], end=" ")

# Linear search
print(list)
search = input("give the input for search: ")

for i in range(0,len(list),1):
    if search == list[i]:
        print("Found at index", i)
        print("Founded at list number", i+1)
        break
    else:
        print("Not found")
