name = input("Enter the name of the student: ")
Reg = input("Enter the registration number: ")
sem = input("Enter the semester : ")

sub1 = int(input("Enter the marks for sub 1: "))
sub2 = int(input("Enter the marks for sub 2: "))
sub3 = int(input("Enter the marks for sub 3: "))
sub4 = int(input("Enter the marks for sub 4: "))
sub5 = int(input("Enter the marks for sub 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
per = float((total_marks/500)*100)
cgpa = float((total_marks/500)*10)
print("|----------------------------------------------------|")
print("\t\tCHANAKYA UNIVERSITY")
print("|----------------------------------------------------|")
print("| \tStudent name:  ", name)
print("| \tStudent registration: ", Reg)
print("| \tSemester: ", sem)

# print("| Marks subject1 ", sub1)

if sub1 >= 90:
    grade = 'A+'
    remark = 'Excellent'
elif sub1 >= 80:
    grade = 'A'
    remark = 'Very Good'
elif sub1 >= 70:
    grade = 'B+'
    remark = 'Good'
elif sub1 >= 60:
    grade = 'B'
    remark = 'Satisfactory'
elif sub1 >= 50:
    grade = 'C'
    remark = 'Needs Improvement'
else:
    grade = 'F'
    remark = 'Failed'

print("| \tSubject 1 grade: " , grade)
# print("Remark :", remark)


# subject 2
# print("| Marks subject2 ", sub2)

if sub2 >= 90:
    grade = 'A+'
    remark2 = 'Excellent'
elif sub2 >= 80:
    grade = 'A'
    remark2 = 'Very Good'
elif sub2 >= 70:
    grade = 'B+'
    remark2 = 'Good'
elif sub2 >= 60:
    grade = 'B'
    remark2 = 'Satisfactory'
elif sub2 >= 50:
    grade = 'C'
    remark2 = 'Needs Improvement'
else:
    grade = 'F'
    remark2 = 'Failed'

print("| \tSubject 2 grade: " , grade)
# print("Remark :", remark)
# subject 3
# print("| Marks subject3 ", sub3)

if sub3 >= 90:
    grade = 'A+'
    remark3 = 'Excellent'
elif sub3 >= 80:
    grade = 'A'
    remark3 = 'Very Good'
elif sub3 >= 70:
    grade = 'B+'
    remark3 = 'Good'
elif sub3 >= 60:
    grade = 'B'
    remark3 = 'Satisfactory'
elif sub3 >= 50:
    grade = 'C'
    remark3 = 'Needs Improvement'
else:
    grade = 'F'
    remark3 = 'Failed'

print("| \tSubject 3 grade: " , grade)
# print("Remark :", remark)
# subject 4
# print("| Marks subject4 ", sub4)

if sub4 >= 90:
    grade = 'A+'
    remark4 = 'Excellent'
elif sub4 >= 80:
    grade = 'A'
    remark4 = 'Very Good'
elif sub4 >= 70:
    grade = 'B+'
    remark4 = 'Good'
elif sub4 >= 60:
    grade = 'B'
    remark4 = 'Satisfactory'
elif sub4 >= 50:
    grade = 'C'
    remark4 = 'Needs Improvement'
else:
    grade = 'F'
    remark4 = 'Failed'

print("| \tSubject 4 grade: " , grade)
# print("Remark :", remark)

# Subject 5

# print("| Marks subject5 ", sub5)

if sub5 >= 90:
    grade = 'A+'
    remark5 = 'Excellent'
elif sub5 >= 80:
    grade = 'A'
    remark5 = 'Very Good'
elif sub5 >= 70:
    grade = 'B+'
    remark5 = 'Good'
elif sub5 >= 60:
    grade = 'B'
    remark5 = 'Satisfactory'
elif sub5 >= 50 :
    grade = 'C'
    remark5 = 'Needs Improvement'
else:
    grade = 'F'
    remark5 = 'Failed'

print("| \tSubject 5 grade: " , grade)
# print("Remark :", remark5)

# Total number
print("| \tTotal marks: ", total_marks)

# Percentage
print("| \tPercentage: ", per, "%")


# CGPA
print("| \tCGPA: ", cgpa, "cgpa")
# Result
if remark=='Failed' or remark2=='Failed' or remark3=='Failed' or remark4=='Failed' or remark5=='Failed':
    print("| \tRemark: Failed")
else:
    print("| \tRemark: Passed")
print("----------------------------------------------------|")