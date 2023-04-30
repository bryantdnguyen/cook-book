#! /usr/bin/env/ python3
import textwrap
from urllib import request, parse  # parse takes out any spaces, parse.quote(foo) EX. IN PDF
from objects import Category, Meal, Area, Instruction, Ingredient, Measure
import json


# ******************************************** CATEGORY **********************************************
def get_category():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"  # API for categories
    file = request.urlopen(url)
    categories = []

    try:
        data = json.loads(file.read().decode('utf-8'))  # Convert JSON format to something readable
        # Fill list with objects containing data from the API
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])
            categories.append(category)
    except(ValueError, KeyError, TypeError):
        return None

    return categories  # Returning list of objects


def get_meal_by_category(category):
    # 'category' will indicate the user's selected category
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    file = request.urlopen(url)
    meals = []

    try:
        data = json.loads(file.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])
            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        return None

    return meals
# ******************************************** CATEGORY **********************************************


# ******************************************** AREA **********************************************
def get_area():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    file = request.urlopen(url)
    areas = []

    try:
        data = json.loads(file.read().decode('utf-8'))
        for area_data in data['meals']:
            area = Area(area_data['strArea'])
            areas.append(area)
    except(ValueError, KeyError, TypeError):
        return None

    return areas


def get_meal_by_area(area):
    # 'area' will indicate the user's selected area
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    file = request.urlopen(url)
    meals = []

    try:
        data = json.loads(file.read().decode('utf-8'))
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])
            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        return None

    return meals
# ******************************************** AREA **********************************************


# ******************************************** RANDOM/SEARCH MEAL **********************************************
def get_search_meal_data(search_meal):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + parse.quote(search_meal)
    file = request.urlopen(url)
    try:
        data = json.loads(file.read().decode('utf-8'))
    except(ValueError, KeyError, TypeError):
        return None

    return data  # Returns readable data from API


def get_random_meal_data():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    file = request.urlopen(url)
    try:
        data = json.loads(file.read().decode('utf-8'))
    except(ValueError, KeyError, TypeError):
        return None

    return data  # Returns readable data from API


def get_random_or_search_meal_name(data):
    meal = ""
    try:
        for meal_data in data['meals']:
            meal = Meal(meal_data['strMeal'])
    except(ValueError, KeyError, TypeError):
        return None

    return meal


def get_random_or_search_meal_instructions(data):
    instructions = []
    try:
        for meal_data in data['meals']:
            instruction = Instruction(meal_data['strInstructions'])
            instructions.append(instruction)
    except(ValueError, KeyError, TypeError):
        return None

    return instructions  # Returns list (should only have 1 object)


def get_random_or_search_meal_ingredients(data):
    ingredients = []
    ingredient_counter = 1
    try:
        while ingredient_counter < 21:  # 20 Ingredients in each data list, some are blank or None
            for meal_data in data['meals']:
                ingredient = Ingredient(meal_data['strIngredient' + str(ingredient_counter)])
                ingredients.append(ingredient)
                ingredient_counter += 1
    except(ValueError, KeyError, TypeError):
        return None

    return ingredients  # Returns list (should have 20 objects)


def get_random_or_search_meal_measures(data):
    measures = []
    measure_counter = 1
    try:
        while measure_counter < 21:  # 20 Measures in each data list, some are blank or None
            for meal_data in data['meals']:
                measure = Measure(meal_data['strMeasure' + str(measure_counter)])
                measures.append(measure)
                measure_counter += 1
    except(ValueError, KeyError, TypeError):
        return None

    return measures  # Return list (should have 20 objects)
# ******************************************** RANDOM/SEARCH MEAL **********************************************
