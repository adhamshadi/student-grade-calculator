print("Student Grade Calculator")

name = input("Enter your name: ")

while True:
try:
number_of_subjects = int(input("Enter the number of subjects: "))

```
    if number_of_subjects > 0:
        break

    print("Please enter a number greater than 0.")

except ValueError:
    print("Please enter a valid number.")
```

grades = []

for i in range(number_of_subjects):
while True:
try:
grade = float(input(f"Enter the grade for subject {i + 1} (0-100): "))

```
        if 0 <= grade <= 100:
            grades.append(grade)
            break

        print("Please enter a grade between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")
```

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

print(f"Highest grade: {max(grades):.2f}")
print(f"Lowest grade: {min(grades):.2f}")
