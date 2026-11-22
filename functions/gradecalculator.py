
def calculate_grade(mark1, mark2, mark3):

    average = (mark1 + mark2 + mark3) / 3

    if average >= 90:
        grade = "A"

    elif average >= 80:
        grade = "B"

    elif average >= 70:
        grade = "C"

    elif average >= 60:
        grade = "D"

    else:
        grade = "F"

    return average, grade


# Taking input
m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

average, grade = calculate_grade(m1, m2, m3)

print("Average marks:", average)
print("Grade:", grade)
