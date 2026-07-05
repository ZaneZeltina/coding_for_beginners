"""
Students grading script
by Zane Zeltina
"""

# Ask student for their grade
mark = int(input("Please enter your test mark (0 - 100)... "))

# Award correct grade

"""
A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: 0 - 59
"""

if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
else:
    grade = "F"

# Print grade to UI / Console
if grade == "F":
    print("Oops! Better luck next time!")
else:
    print("Well done! You earned a grade of: " + grade)
