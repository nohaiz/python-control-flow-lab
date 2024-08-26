# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    vowels = ["a","e","i","o","u"]
    consonants = ['b','c','d','f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't','v', 'w', 'x', 'y', 'z']

    if letter.isalpha():
      for vowel in vowels: 
        if letter == vowel:
            print(f'This letter "{letter}" is a vowel.')
            break
      for consonant in consonants:
        if letter == consonant: 
            print(f'This letter "{letter}" is a consonant.')
            break
    else:
       print(f'Invalid entry "{letter}".')

# Call the function
# check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age_str = input("Please enter your age: ")
    voting_age = 18

    if not age_str.isdigit():
       print(f'Invalid entry')
    else :
       age = int(age_str)

       if age >= voting_age:
          print(f'You are {age} and eligible to vote')
       else:
          print(f'You are {age} and not eligible to vote')

# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_string = input("Enter a dog's age: ")
    if not dog_string.isdigit():
       print("Invalid input")
    else:
       dog_age= int(dog_string)
       if dog_age == 1 or dog_age == 2:
          dog_year= dog_age * 10
       else:
          dog_year = 20 + (dog_age - 2) * 7  
    print(f"The dog's age in dog years is {dog_year}")

# Call the function
# calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.


def weather_advice():
    # Your control flow logic goes here
    weather_cold = input("Is it cold? ").lower().strip()
    weather_raining = input("Is it raining? ").lower().strip()

    
    if weather_cold not in ['yes', 'no'] or weather_raining not in ['yes', 'no']:
        print("Invalid input")
        return
  
    if weather_cold == 'yes' and weather_raining == 'yes':
      print("Wear a waterproof coat.")
    elif weather_cold == 'yes' and weather_raining == 'no':
      print("Wear a warm coat.")
    elif weather_cold == 'no' and weather_raining == 'yes':
      print("Carry an umbrella.")
    elif weather_cold == 'no' and weather_raining == 'no':
      print("Wear light clothing.")

# Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }

    month_str = input("Enter the month of the year (Jan - Dec): ").lower()
    day_str = input("Enter the day of the month: ")

    if month_str not in months:
        print("Invalid month.")
        return

    if not day_str.isdigit():
        print("Invalid day.")
        return

    day = int(day_str)

    if day < 1 or day > 31:
        print("Invalid day.")
        return

    month = months[month_str]
    season = ""

    if (month == 12 and day >= 21) or (month == 1) or (month == 2) or (month == 3 and day <= 19):
        season = "Winter"
    elif (month == 3 and day >= 20) or (month == 4) or (month == 5) or (month == 6 and day <= 20):
        season = "Spring"
    elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day <= 21):
        season = "Summer"
    elif (month == 9 and day >= 22) or (month == 10) or (month == 11) or (month == 12 and day <= 20):
        season = "Fall"
    else:
        print("Invalid date")
        return
    print(f"{month_str.capitalize()} {day:02d} is in {season}.")

# Call the function
determine_season()