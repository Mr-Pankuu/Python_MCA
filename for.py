# Start from 0 to 99

# for i in range(100):
#     print(i)

# If we want to print some of the starting numberes so

# for i in range(22, 100):
#     print(i)

#  For half pyramid
# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     print()
#     for j in range(1, i+1, 1):
#         print(j, end=" ")

# For half pyramid but same number of iterations

# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     print()
#     for j in range(1, i+1, 1):
#         print(i, end=" ")

# For square
# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     print()
#     for j in range(i, i+n, 1):
#         p=j%n
#         if p==0:
#             p=n
#         print(p, end=" ")
        
# Output
# 1 2 3 4 5 
# 2 3 4 5 1 
# 3 4 5 1 2 
# 4 5 1 2 3 
# 5 1 2 3 4 

# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     if i%5 == 0:
#         print(i)

#     else:
#         print(i , end=" ")

# Output
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20

# For one sided 
# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):

#     p= "\t"
#     print(i)
#     for j in range(1, i+1, 1):
#         print(p, end=" ")
#     p=p+p

# Output
# 1
#          2
#                  3
#                          4
#                                  5


# For one sided pyramid use 2 numbers
# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     p= "\t"
#     # print(i , i+1)
#     if i%2 == 0:
#         # print(i , i+1)
#         for j in range(1, i+1, 1):
#             print(p, end=" ")
#     else:
#         print(i , i+1)
#     p=p+p

# For one sided pyramid and also one sided pyramid in opposite directions

# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     print()
#     for j in range(1, i+1, 1):
#         print(j, end=" ")
# for i in range(n-1 , 0 , -1):
#     print()
#     for j in range(1, i+1, 1):
#         print(j, end=" ")

# Output
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1


# For one sided pyramid and also one sided pyramid in opposite directions with same number 

# n = int(input("Enter the limit :"))
# for i in range(1 , n+1 , 1):
#     print()
#     for j in range(1, i+1, 1):
#         print(i, end=" ")
# for i in range(n-1 , 0 , -1):
#     print()
#     for j in range(1, i+1, 1):
#         print(i, end=" ")

