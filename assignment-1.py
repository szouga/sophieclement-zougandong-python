#Section 1
name = "Student"
age = 40
height = "5.7"
is_student = True

#Section 2
name = input("Please enter your name: ")
year_of_birth = input("Please enter the year you were born: ")
convert_age = int(year_of_birth)
current_year = 2026
age = current_year - convert_age
print(f"Hello, {name}! You are approximately {age} years old.")
