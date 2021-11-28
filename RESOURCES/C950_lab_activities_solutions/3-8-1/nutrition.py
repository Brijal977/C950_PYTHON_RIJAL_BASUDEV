class Food:
    def __init__(self, name, protein, fat, carbs, calories):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.calories = calories
        self.set_fraction(1.0)

    def set_fraction(self, fraction):
        self.fraction = fraction
        self.protein_calories = 4 * fraction * self.protein
        self.carbs_calories = 4 * fraction * self.carbs
        self.fat_calories = 9 * fraction * self.fat
        self.calories = fraction * self.calories

    def __str__(self):
        return "[%0.4f] %s (P=%s,C=%s,F=%s,E=%s)" % (
        self.fraction, self.name, self.protein, self.carbs, self.fat, self.calories)


class MealPlan:
    def __init__(self):
        self.foods = []
        self.total_calories = 0.0
        self.total_protein_calories = 0.0
        self.total_carbs_calories = 0.0
        self.total_fat_calories = 0.0

    def add_food(self, food):
        self.foods.append(food)
        self.total_protein_calories += food.protein_calories
        self.total_carbs_calories += food.carbs_calories
        self.total_fat_calories += food.fat_calories
        self.total_calories += food.calories

    def percent_nutrient(self, nutrient):
        if self.total_calories > 0.0:
            return getattr(self, "total_%s_calories" % nutrient) / self.total_calories
        else:
            return 0.0

    def calories_with_food(self, food):
        return self.total_calories + food.calories

    def percent_nutrient_with_food(self, food, nutrient):
        if self.total_calories + food.calories > 0.0:
            return (getattr(self, "total_%s_calories" % nutrient) + getattr(food, "%s_calories" % nutrient)) / (
                        self.total_calories + food.calories)
        else:
            return 0.0

    def fraction_to_fit_calories_limit(self, food, calorie_limit):
        if food.calories == 0: return 1.0
        fraction = (calorie_limit - self.total_calories) / food.calories
        if fraction >= 1.0:
            return 1.0
        elif fraction <= 0.0:
            return 0.0
        else:
            return fraction

    def fraction_to_fit_nutrient_goal(self, food, nutrient, goal):
        denominator = getattr(food, "%s_calories" % nutrient) - goal * food.calories
        if denominator == 0: return 1.0
        fraction = (goal * self.total_calories - getattr(self, "total_%s_calories" % nutrient)) / denominator
        if fraction >= 1.0:
            return 1.0
        elif fraction <= 0.0:
            return 0.0
        else:
            return fraction

    def meets_calorie_limit(self, calorie_limit, threshold):
        diff = calorie_limit - self.total_calories
        return -threshold <= diff and diff <= threshold

    def meets_nutrient_goal(self, nutrient, goal, threshold):
        diff = goal - self.percent_nutrient(nutrient)
        return -threshold <= diff and diff <= threshold

    def __str__(self):
        s = ""
        if len(self.foods) == 0: return "Empty Plan"
        item = 1
        for food in self.foods:
            s += "%d: %s\n" % (item, food)
            item += 1

        s += "Total Calories: %s\n" % self.total_calories
        s += "\tProtein: %s\n" % self.percent_nutrient("protein")
        s += "\tCarbs: %s\n" % self.percent_nutrient("carbs")
        s += "\tFat: %s" % self.percent_nutrient("fat")

        return s
