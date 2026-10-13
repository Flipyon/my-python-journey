# Student Average Calculator - By Flipyon
print("=== STUDENT AVERAGE CALCULATOR ===")

def calculate_average(scores):
    total = sum(scores)
    avg = total / len(scores)
    return avg

def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Main program
name = input("Enter student name: ")
n = int(input("How many subjects? "))

marks = []
for i in range(n):
    m = int(input(f"Enter mark for subject {i+1}: "))
    marks.append(m)

average = calculate_average(marks)
grade = get_grade(average)

print("\n--- RESULT ---")
print(f"Student: {name}")
print(f"Marks: {marks}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}") 
