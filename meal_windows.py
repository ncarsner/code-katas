import random
from datetime import datetime

# Define meal lists
breakfast_meals = [
    "Tofu with vegetables, whole wheat toast",
    "Greek yogurt parfait with granola and mixed berries",
    "Whole grain waffles with berries and Greek yogurt",
    "Spinach and feta omelette, whole wheat toast",
    "Oatmeal, sliced bananas and walnuts",
    "3 egg whites, 2 slices whole wheat toast, 1/4 avocado",
    "Cottage cheese pancakes with maple syrup and mixed berries",
    "Greek yogurt with honey, granola, and mixed berries",
    "Whole grain toast, mashed avocado, sliced tomatoes",
    "Scrambled eggs, smoked salmon, whole wheat muffin, 1 TBSP cream cheese",
    "Breakfast burrito (scrambled eggs, black beans, salsa, whole wheat tortilla), 1/4 avocado",
    "Breakfast smoothie (banana, spinach, protein powder, almond milk), 1 slice whole grain toast",
]

snack1_meals = [
    "1 piece fruit, 1/2 cup cottage cheese/Greek yogurt, 1 oz mixed nuts/1 TBSP almond/peanut butter",
    "Veggie sticks, 2 TBSP hummus, 1 oz. mixed nuts",
    "6-10 whole grain crackers, 2 slices cheese, 1/2 cup grapes",
    "2 hard-boiled eggs, 1/2 cup cherry tomatoes, 1 slice whole grain toast, 1/4 avocado",
    "Greek yogurt smoothie: 1 cup spinach, 1 banana, 1 scoop protein powder",
    "1 slice whole grain toast, 1/2 cup cottage cheese, 1/2 cup sliced fruit",
    # "Homemade trail mix: 1/4 cup dried fruits, 1/4 cup mixed nuts, 1 TBSP dark chocolate chips",
    "2 bell peppers, 1/2 cup cottage cheese, 1/2 cup mixed berries",
    "Quinoa salad: 1/2 cup quinoa, 1/2 cucumber, 1/2 cup cherry tomatoes, 1/4 cup feta, balsamic vinaigrette",
    "Greek yogurt parfait: 1/2 cup granola, 1/2 cup mixed berries, honey",
]

lunch_meals = [
    "Chicken breast, 1 cup quinoa, 1 cup steamed broccoli",
    "Turkey and avocado wrap, mixed greens salad",
    "Shrimp and avocado salad, whole grain roll",
    "Quinoa and black bean salad with mixed greens",
    "Chicken Caesar salad with whole grain croutons",
    "Grilled vegetable quinoa bowl, mixed greens salad with vinaigrette",
    "Tuna salad wrap with whole wheat tortilla, mixed greens salad, olive oil dressing",
    "Grilled shrimp skewers, brown rice, steamed asparagus",
    "Lentil soup, whole grain roll, side salad with balsamic vinaigrette",
    "Chickpea, avocado, and mixed greens salad with lemon vinaigrette",
    "Grilled chicken thighs, quinoa, roasted Brussels sprouts",
    "Quinoa salad with chickpeas, tomatoes, cucumbers, feta cheese, olive oil dressing",
    "Turkey burger, whole grain bun, mixed greens salad with vinaigrette",
    "Salmon fillet, brown rice, roasted sweet potatoes",
    "Turkey breast sandwich, whole grain bread, mixed greens salad with olive oil dressing",
    "Chicken and vegetable stir-fry, brown rice, steamed broccoli",
    "Grilled veggie wrap with hummus, mixed green salad with vinaigrette",
]

snack2_meals = [
    "1 piece fruit, 1/2 cup cottage cheese/Greek yogurt, 1 TBSP almond/peanut butter",
    # "1 whole grain rice cake, 2 TBSP hummus, cucumber slices",
    # "Whole wheat pita, 1/4 cup of tzatziki sauce, carrot sticks",
    # "1 cup of edamame (steamed soybeans) with a sprinkle of sea salt",
    "1 oz. dark chocolate, 1/4 cup mixed berries",
    "1 slice whole grain bread, 1/4 avocado, tomato slices",
    # "1 small bowl of air-popped popcorn seasoned with nutritional yeast",
    "Handful roasted chickpeas, squeeze of lemon juice",
    "1 hard-boiled egg with paprika, baby carrots",
    "1/2 cup cottage cheese/Greek yogurt, cucumber slices with olive oil",
    "1 whole wheat tortilla, 2 TBSP hummus, bell pepper strips",
]

dinner_meals = [
    "Baked salmon, quinoa, steamed asparagus",
    "Grilled steak, sweet potato fries, sautéed spinach",
    "Baked cod, sweet potato mash, roasted cauliflower",
    "Grilled tofu, brown rice, sautéed zucchini",
    "Baked chicken thighs, brown rice, sautéed kale",
    "Grilled salmon, brown rice, roasted sweet potatoes",
    "Baked chicken breast, quinoa, sautéed broccoli",
    "Baked tilapia, brown rice and sautéed kale",
    "Grilled chicken thighs, quinoa and roasted Brussels sprouts",
    "Baked pork loin, quinoa salad and steamed green beans",
    "Baked chicken breast, Quinoa, steamed broccoli",
    "Beef stir-fry, vegetables, cooked noodles, sesame oil",
    "Lentil soup,  whole grain roll, side salad with balsamic vinaigrette",
    "Chicken stir-fry with vegetables, brown rice with teriyaki sauce",
    "Baked cod, quinoa, roasted cauliflower",
    "Baked pork loin, quinoa, roasted Brussels sprouts",
    "Baked halibut, brown rice, sautéed kale",
    "Turkey chili, cornbread muffin, steamed green beans",
]

# Define time windows for meal categories
time_windows = {
    "Breakfast": (4, 9),
    "Snack1": (10, 11),
    "Lunch": (11, 13),
    "Snack2": (14, 16),
    "Dinner": (17, 20)
}

# Define encouragement messages
encouragements = [
    "Don't overeat!",
    "Let's wait awhile.",
    "It's not too long to wait.",
    "You'll feel better if you wait.",
    "Just a little bit longer.",
    "We're not ready to eat yet.",
    "No, not yet.",
    "You'll look fitter if you wait a little.",
    "Not yet.",
    "Hold on for a bit.",
    "You're not hungry right now.",
    "Drink some water.",
    "Remember to space out your intake.",
]

# Function to convert time to relative AM/PM format
def convert_to_ampm(hour):
    if hour < 12:
        return f"{hour} am"
    elif hour == 12:
        return "12 pm"
    else:
        return f"{hour - 12} pm"

# Get meal based on current time
def get_meal(hour_of_day):
    for meal_category, (start_hour, end_hour) in time_windows.items():
        if start_hour <= hour_of_day < end_hour:
            if meal_category == "Breakfast":
                return random.choice(breakfast_meals)
            elif meal_category == "Snack1":
                return random.choice(snack1_meals)
            elif meal_category == "Lunch":
                return random.choice(lunch_meals)
            elif meal_category == "Snack2":
                return random.choice(snack2_meals)
            elif meal_category == "Dinner":
                return random.choice(dinner_meals)
    return random.choice(encouragements)


# Get the current hour
current_hour = datetime.now().hour

# Get meal for the current time
current_meal = get_meal(current_hour)

# Print the selected meal along with the relative AM/PM format of the current time
print(f"{convert_to_ampm(current_hour)}: {current_meal}")