A = [0,1,2,3,4,5,6,7]
B = [x for x in A]

print(B)
# squares
# Redefine array A!!!!
A = [x*x for x in A]
print(A)

First = [1,2]
Second = [3,4]
Third = [5,6]

# Merging a 2D array in Python into one string with List Comprehension
A = [item for lst in (First, Second, Third) for item in lst]
print(A)