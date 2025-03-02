from django.shortcuts import render
from django.http import JsonResponse
import json

# Organize the data into three separate lists
restaurants = [
    "Dunkin", "Dunkin", "Dunkin", "Dunkin", "Dunkin",
    "Raising Canes", "Raising Canes", "Raising Canes", "Raising Canes", "Raising Canes",
    "Wendy's", "Wendy's", "Wendy's", "Wendy's", "Wendy's",
    "McDonald's", "McDonald's", "McDonald's", "McDonald's", "McDonald's",
    "Chick-fil-A", "Chick-fil-A", "Chick-fil-A", "Chick-fil-A", "Chick-fil-A"
]

food_types = [
    "Glazed Donut", "Chocolate Creme Donut", "Vanilla Frosted Donut", "Bavarian Kreme Donut", "Double Chocolate Donut",
    "3 Finger Combo", "Box Combo", "Sandwich Combo", "Chicken Sandwich", "Texas Toast",
    "Dave's Single", "Bacon Double Stack", "Classic Chicken Sandwich", "Crispy Chicken BLT", "Dave's Double",
    "Big Mac", "Quarter Pounder with Cheese", "World Famous Fries (M)", "Chicken McNuggets (10 pieces)", "Filet O Fish",
    "Original Chick-fil-A Chicken Sandwich", "Chick-fil-A Nuggets", "Spicy Chicken Sandwich", "Chicken Strips", "Waffle Fries"
]

nutritional_facts = [
    {'calories': 240, 'carbs': 33, 'protein': 13, 'fat': 11, 'sodium': 270, 'fiber': 4},
    {'calories': 290, 'carbs': 36, 'protein': 14, 'fat': 14, 'sodium': 300, 'fiber': 5},
    {'calories': 260, 'carbs': 34, 'protein': 14, 'fat': 11, 'sodium': 280, 'fiber': 4},
    {'calories': 240, 'carbs': 31, 'protein': 11, 'fat': 11, 'sodium': 310, 'fiber': 4},
    {'calories': 380, 'carbs': 41, 'protein': 22, 'fat': 23, 'sodium': 430, 'fiber': 4},
    
    {'calories': 1050, 'carbs': 83, 'protein': 9, 'fat': 59, 'sodium': 1730, 'fiber': 48},
    {'calories': 1290, 'carbs': 98, 'protein': 17, 'fat': 72, 'sodium': 2280, 'fiber': 62},
    {'calories': 1140, 'carbs': 98, 'protein': 14, 'fat': 72, 'sodium': 1740, 'fiber': 51},
    {'calories': 830, 'carbs': 69, 'protein': 14, 'fat': 41, 'sodium': 1500, 'fiber': 47},
    {'calories': 150, 'carbs': 23, 'protein': 4, 'fat': 4.5, 'sodium': 300, 'fiber': 4},
    
    {'calories': 570, 'carbs': 38, 'protein': 8, 'fat': 34, 'sodium': 1020, 'fiber': 29},
    {'calories': 480, 'carbs': 26, 'protein': 6, 'fat': 29, 'sodium': 840, 'fiber': 29},
    {'calories': 490, 'carbs': 49, 'protein': 5, 'fat': 21, 'sodium': 1450, 'fiber': 28},
    {'calories': 410, 'carbs': 34, 'protein': 5, 'fat': 23, 'sodium': 920, 'fiber': 19},
    {'calories': 810, 'carbs': 39, 'protein': 6, 'fat': 51, 'sodium': 1190, 'fiber': 49},
    
    {'calories': 580, 'carbs': 45, 'protein': 7, 'fat': 34, 'sodium': 1060, 'fiber': 25},
    {'calories': 520, 'carbs': 42, 'protein': 10, 'fat': 26, 'sodium': 1140, 'fiber': 30},
    {'calories': 320, 'carbs': 43, 'protein': 0, 'fat': 15, 'sodium': 260, 'fiber': 5},
    {'calories': 410, 'carbs': 26, 'protein': 0, 'fat': 24, 'sodium': 850, 'fiber': 23},
    {'calories': 380, 'carbs': 38, 'protein': 4, 'fat': 19, 'sodium': 580, 'fiber': 16},
    
    {'calories': 420, 'carbs': 41, 'protein': 6, 'fat': 18, 'sodium': 1460, 'fiber': 29},
    {'calories': 160, 'carbs': 7, 'protein': 1, 'fat': 7, 'sodium': 760, 'fiber': 17},
    {'calories': 450, 'carbs': 45, 'protein': 6, 'fat': 19, 'sodium': 1730, 'fiber': 28},
    {'calories': 200, 'carbs': 11, 'protein': 1, 'fat': 9, 'sodium': 580, 'fiber': 19},
    {'calories': 365, 'carbs': 48, 'protein': 0.4, 'fat': 17, 'sodium': 246, 'fiber': 4}
]


# View to get food data based on the selected food item
def get_food_data(request):
    selected_food = request.GET.get('food')  # Get the selected food item from the request
    
    # Find matching data for the selected food item
    food_data = None
    for i, food in enumerate(food_types):
        if food == selected_food:
            food_data = {
                'restaurant': restaurants[i],
                'food_item': food,
                'calories': nutritional_facts[i]['calories'],
                'carbs': nutritional_facts[i]['carbs'],
                'protein': nutritional_facts[i]['protein'],
                'fat': nutritional_facts[i]['fat'],
                'sodium': nutritional_facts[i]['sodium'],
                'fiber': nutritional_facts[i]['fiber']
            }
            break
    
    if food_data:
        return JsonResponse(food_data)
    else:
        return JsonResponse({'error': 'Food item not found'}, status=404)

# Other views (e.g., calculate_insulin) can be added similarly
from django.shortcuts import render
import json

def home(request):
    return render(request, 'HomePage/home.html', {
        'restaurants': json.dumps(restaurants),
        'food_types': json.dumps(food_types),
        'nutritional_facts': json.dumps(nutritional_facts)
    })

