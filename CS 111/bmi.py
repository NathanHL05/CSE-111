# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def get_height_units():
    while True:
        try:
            unit = int(input("In which unit will you enter weight? Enter 1 for feet and inches, 2 for cm: "))
            return unit
        except ValueError:
             print("Please enter a valid value.")

def get_height(units):
    if units == 1:
        feet = int(input("Enter your height in feet(do not add inches yet): "))
        inches = int(input(f"Enter how many inches on top of {feet} feet: "))
        inches = (feet * 12) + inches
        height_cm=cm_from_in(inches)
        return height_cm
    else:
        height_cm = int(input("Enter your height in cm: "))
        return height_cm




def get_weight():
    while True:
        try:
            weight = float(input("What is your weight: "))
            return weight
        except ValueError:
             print("Please enter a valid weight")
    

def get_weight_unit():
    while True:
        try:
            unit = int(input("In which unit will you enter weight? Enter 1 for lbs, 2 for Kg, 3 for Stone: "))
            return unit
        except ValueError:
             print("Please enter a valid value. Enter 1 for lbs, 2 for Kg, 3 for Stone: ")
            
def convert_to_kg(unit, weight):
    if unit == 1:
        weight = kg_from_lb(weight)
        return weight
    elif unit == 3:
        weight = kg_from_stone(weight)
        return weight
    else:
        return weight
    
def kg_from_lb(lbs):
    kg = lbs * 0.453592
    return kg

def kg_from_stone(stones):
    kg = stones * 6.35029
    return kg





def basal_metabolic_rate(gender, weight, height, age):

    if gender == "M":
        kcals_per_day = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "F":
        kcals_per_day = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return kcals_per_day

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches * 2.54

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    BMI = (10000* weight) / (height**2)
    return BMI


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def get_gender():
    while True:
        try:
            gender = input("Enter gender (M/F): ")
            return gender
        except (gender != "M" or gender != "F"):
            print("Please enter a valid input")


def main():
    birth_str = input("what is your birth date (y-m-d)")
    gender = get_gender()
    unit = get_weight_unit()
    weight = get_weight()
    weight_in_kg = convert_to_kg(unit,weight)
    height_unit = get_height_units()
    height_cm = get_height(height_unit)
    age =  compute_age(birth_str)
    bmi = body_mass_index(weight_in_kg, height_cm)
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_in_kg}")
    print(f"Height (cm) {height_cm}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender, weight_in_kg, height_cm, age):1f}")

main()