print("Student Grade Calculator")

name = input("Enter your name: ")

number_of_subjects = int(input("Enter the number of subjects: "))

grades = []

for i in range(number_of_subjects):
    grade = float(input(f"Enter the grade for subject {i + 1}: "))
    grades.append(grade)

average = sum(grades) / number_of_subjects

print("\n--- Results ---")
print(f"Student: {name}")
print(f"Average: {average:.2f}")

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")
