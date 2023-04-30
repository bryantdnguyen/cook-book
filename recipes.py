#! /usr/bin/env/ python3
import textwrap
import requests


def display_title():
    print("My Recipe Program")
    print()


def display_menu():
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("7 - Menu")
    print("0 - Exit the Program")
    print()


# ******************************************** SIMPLE DISPLAY **********************************************
def display_categories(categories):
    print("\nCATEGORIES:")
    for i in range(len(categories)):
        print(" ", str(categories[i].get_category_name()))
    print()


def display_areas(areas):
    print("\nAreas:")
    for i in range(len(areas)):
        print(" ", str(areas[i].get_area_name()))
    print()


def display_meals(title, meals):
    print("\n" + title.upper(), "MEALS")
    for i in range(len(meals)):
        print(" ", str(meals[i].get_meal_name()))
    print()
# ******************************************** SIMPLE DISPLAY **********************************************


# ******************************************** DISPLAY BY USER SELECTION **********************************************
def display_meal_by_category(categories):
    isFound = False
    user_category_choice = input("Enter a Category: ")

    for i in range(len(categories)):
        category = categories[i]
        if category.get_category_name().lower() == user_category_choice.lower():
            isFound = True
            break

    if isFound:
        meals = requests.get_meal_by_category(user_category_choice)
        display_meals(user_category_choice, meals)  # Call to display meals
    else:
        print("\nInvalid category, please try again.")


def display_meal_by_area(areas):
    isFound = False
    user_area_choice = input("Enter an Area: ")

    for i in range(len(areas)):
        area = areas[i]
        if area.get_area_name().lower() == user_area_choice.lower():
            # If user's requested meal is found within the list, flag isFound to be true
            isFound = True
            break  # End the loop

    if isFound:
        meals = requests.get_meal_by_area(user_area_choice)  # List of meals based on user's AREA choice
        display_meals(user_area_choice, meals)  # Call to display meals
    else:
        print("\nInvalid area, please try again.")
# ******************************************** DISPLAY BY USER SELECTION **********************************************


# ******************************************** DISPLAY BY SEARCH/RANDOM **********************************************
def display_random_meal():
    data = requests.get_random_meal_data()
    names = requests.get_random_or_search_meal_name(data)
    instructions = requests.get_random_or_search_meal_instructions(data)
    ingredients = requests.get_random_or_search_meal_ingredients(data)
    measures = requests.get_random_or_search_meal_measures(data)

    display_recipe(names, instructions, ingredients, measures)


def display_search_meal():
    isFound = False
    user_meal_choice = input("Enter Meal Name: ")
    data = requests.get_search_meal_data(user_meal_choice.lower())

    while data['meals'] is None:  # Loop until SEARCHED MEAL is within the data
        print("Error. Meal not found, please try again.")
        user_meal_choice = input("Enter Meal Name: ")
        data = requests.get_search_meal_data(user_meal_choice.lower())  # Exit condition, data must not return None

    if data['meals'] is not None:
        isFound = True  # Searched Meal exists, flag isFound to be true

    if isFound:
        # Retrieve Meal name, instructions, ingredients, measures & display
        names = requests.get_random_or_search_meal_name(data)
        instructions = requests.get_random_or_search_meal_instructions(data)
        ingredients = requests.get_random_or_search_meal_ingredients(data)
        measures = requests.get_random_or_search_meal_measures(data)

        display_recipe(names, instructions, ingredients, measures)


def display_recipe(meal, instructions, ingredients, measures):
    # Printing Recipe: MEAL NAME
    print("\nRecipe: " + str(meal.get_meal_name()))

    # Printing Instructions, line capped at 80 characters
    print("\nInstructions:")
    my_wrap = textwrap.TextWrapper(width=80)
    wrap_list = my_wrap.wrap(str(instructions[0].get_instruction()))
    for line in wrap_list:
        print(line)
    print()

    # Printing Ingredients, which includes list of measure and list of ingredient
    print("Ingredients: ")
    print("{:35} {:>1} {:20}".format("Measure", " ", "Ingredient"))
    print("-"*80)
    for i in range(20):  # Loop 20 times  range(len(ingredients))
        ingredient = ingredients[i].get_ingredient()  # Assign Object's name to variable
        measure = measures[i].get_measure()           # Assign Object's name to variable

        # Only print if the variable's name isn't empty and doesn't include 'None'
        if(str(ingredient).lower() != "" and ingredient is not None) and \
                (str(measure).lower() != "" and measure is not None):
            print("{:35} {:>1} {:20}".format(str(measure), " ", str(ingredient)))
    print()
# ******************************************** DISPLAY BY SEARCH/RANDOM **********************************************


def main():
    display_title()
    display_menu()

    categories = requests.get_category()  # List of Categories
    areas = requests.get_area()           # List of Areas

    while True:
        user_choice = input("What would you like to do?: ")
        if user_choice == "1":
            display_categories(categories)
        elif user_choice == "2":
            display_meal_by_category(categories)
        elif user_choice == "3":
            display_search_meal()
        elif user_choice == "4":
            display_random_meal()
        elif user_choice == "5":
            display_areas(areas)
        elif user_choice == "6":
            display_meal_by_area(areas)
        elif user_choice == "7":
            display_menu()
        elif user_choice == "0":
            print("Thanks for coming, Bye!")
            break
        else:
            print("Please enter a valid choice.\n")


if __name__ == "__main__":
    main()
