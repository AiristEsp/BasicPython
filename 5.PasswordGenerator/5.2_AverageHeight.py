# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

number_of_student = len(student_heights)
#total_heights = sum(student_heights)

total_height = 0
for height in student_heights:
    total_height += height


total_student = 0
for student in student_heights:
    total_student += 1


average_height = round(total_height / number_of_student)
print(average_height)
