import sys, operator, random
from nutrition import Food, MealPlan

NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000


def load_nutrient_data(filename):
    foods = []
    with open(filename, "r") as f:
        for line in f:
            if len(line) > 0:
                parts = line.split(":")
                name = ":".join(parts[0:-1])
                rest = parts[-1]
                protein, fat, carbs, calories = map(float, rest.split(","))
                foods.append(Food(name, protein, fat, carbs, calories))
    return foods


def sort_food_list(foods, nutrient):
    foods.sort(key=operator.attrgetter(nutrient + "_calories"), reverse=True)


def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()

    sort_food_list(foods, nutrient)
    for food in foods:
        if food.calories == 0 and getattr(food, nutrient) == 0: continue

        # Calculate the fraction of this food allowed to fit the calorie limit.
        fraction_calories = plan.fraction_to_fit_calories_limit(food, MAX_CALORIES)

        # Check if the whole portion fits.
        if fraction_calories >= 1.0:

            # The whole portion fits as far as calories are concerned. Check to see
            # if the portion would surpass the nutrient goal.
            if plan.percent_nutrient_with_food(food, nutrient) <= nutrient_goal + NUTRIENT_THRESHOLD:
                # The whole item fits. Add it to the meal plan, and continue on.
                plan.add_food(food)
            else:
                # Only a fraction of the portion will fit. Calculate the fraction that will fit
                # with respect to the nutrient.
                fraction_nutrient = plan.fraction_to_fit_nutrient_goal(food, nutrient, nutrient_goal)

                # If the fraction isn't trivial, officially set the fraction of the food item and
                # add it to the meal plan.
                if fraction_nutrient > FRACTION_THRESHOLD:
                    food.set_fraction(fraction_nutrient)
                    plan.add_food(food)
        else:
            # There are too many calories in a single portion of this food. Check if the
            # fraction required to hit the calorie target exactly is trivial.
            if fraction_calories > CALORIE_THRESHOLD:

                # Calculate the fraction of a portion needed to hit the nutrient goal exactly,
                # and see if it is non-trivial.
                fraction_nutrient = plan.fraction_to_fit_nutrient_goal(food, nutrient, nutrient_goal)
                if fraction_nutrient > FRACTION_THRESHOLD:
                    # Officially set the food item's fraction to whichever is smaller between
                    # the total calorie fraction and the nutrient fraction, and add to
                    # the meal plan.
                    food.set_fraction(min(fraction_calories, fraction_nutrient))
                    plan.add_food(food)

        # Check if we've reached both goals. If both calories and nutrient composition meet the
        # goals, exit the loop.
        if plan.meets_calorie_limit(MAX_CALORIES, CALORIE_THRESHOLD) and plan.meets_nutrient_goal(nutrient,
                                                                                                  nutrient_goal,
                                                                                                  NUTRIENT_THRESHOLD): break

    return plan


def print_menu():
    print()
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbs")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()


if __name__ == "__main__":

    filename = input("Enter name of food data file: ")
    foods = load_nutrient_data(filename)

    choice = -1
    while choice < 1 or choice > 3:
        print_menu()
        try:
            choice = int(input("Enter choice (1-4): "))
        except:
            choice = -1
        if choice == 1:
            nutrient = "protein"
        elif choice == 2:
            nutrient = "carbs"
        elif choice == 3:
            nutrient = "fat"
        elif choice == 4:
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice! Enter an integer from 1-4!")

    nutrient_goal = None
    while nutrient_goal is None:
        try:
            nutrient_goal = float(input("What percentage of calories from %s is the goal? " % nutrient)) / 100.0
            if nutrient_goal < 0.0 or nutrient_goal > 1.0: nutrient_goal = None
        except:
            pass

    plan = create_meal_plan(foods, nutrient, nutrient_goal)
    print(plan)