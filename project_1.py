score: int = int(input("enter your exam score(0-100): "))
age: int = int(input("enter your age: "))
print("\n--Evaluation report---")
if score >= 90 and score <= 100:
    grade: str = "A+ (Excellent)"
elif score >= 75 and score < 90:
    grade: str = "B (Good)"
elif score >= 50 and score < 75:
    grade: str = "C (Pass)"
elif score >= 0 and score < 50:
    grade: str = "F (Fail)"
else:
    grade: str = "Invalid score!"
print(f"Grade Result: {grade}")
role_code: int = int(input("\nEnter you role code (1:student,2:developer,3:admin): "))
match role_code:
    case 1:
        role: str = "student"
    case 2:
        role: str = "developer"
    case 3:
        role: str = "admin"
    case _:
        role: str = "Guest"
print(f"user access role: {role}")
    
