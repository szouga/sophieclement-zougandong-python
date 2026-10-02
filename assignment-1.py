#assignment-1.py
name = input("What is your name?: ")
birth_year = int(input("What is the year you were born?: "))
first_num = float(input("Enter your first number: "))
second_num = float(input("Enter your second number: "))

first_name = input("Please provide your first name: ").capitalize()
last_name = input("Please provide your last name: ").capitalize()
#hometown_city = input("Type your city: ").capitalize()
#hometown_state = input("Type your state: ").upper()
hometown = input("What city and state do you reside in?: ").capitalize()
hobby = input("Enter your favorite hobby: ").capitalize()
fun_fact = input("Give me a fun fact about yourself: ").capitalize()

#multiply_num = first_num * second_num
current_year = 2026
item = "Basket of Fries"
price = 9
quantity = 1
total = price * quantity

full_name = first_name + " " + last_name
#hometown = f"{hometown_city}, {hometown_state}"

#section one
age = 26
height = 5.2
is_student = False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#section two
print(f"Hi, {name}! You are approximately {current_year - birth_year} years old.")
#section 3
print(f"{first_num * second_num}")

#section 4

print("========================")
print("       RECEIPT     ")
print("========================")
print(f"Item:      ${item}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  ${quantity:.2f}")
print("------------------------")
print(f"Total:     ${total:.2f}")

#section 5
print("╔══════════════════════════════╗")
print(f"     PROFILE: {full_name}    ")
print("╚══════════════════════════════╝")
print(f"Hometown:  {hometown}")
print(f"Hobby:     {hobby}")
print(f"Fun Fact:  {fun_fact}.")
print(f"Age:       {current_year - birth_year}")

