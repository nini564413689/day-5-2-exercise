# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# for max in range (0, len (student_scores)-1):

#   if student_scores[max] > student_scores[max+1]:
#      Max_score = student_scores[max]


# print (f"The highest score in the class is: {Max_score}")

# method 2:
Max_score = 0
for Max in student_scores:
  if Max > Max_score:
    Max_score = Max

print (f"The highest score in the class is: {Max_score}")