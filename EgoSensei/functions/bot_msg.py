def format_response(raw_data,category: str) -> str:
   
    # Check if it's food data (longer sublists)
    if category == 'analytics':
        format_training_data(raw_data)
    elif category == 'diet':
        return format_food_data(raw_data)
    elif category == 'training':
        return format_training_data(raw_data)
    elif category == 'cardio':
        return format_cardio(raw_data)
    
def format_food_data(food_list: list) -> str:
    """Formats food nutrition data"""
    lines = []
    for item in food_list:
        try:
            name = item[1]
            serving = item[3]
            calories = (item[2] * serving) / 100
            protein = (item[4] * serving) / 100
            carbs = (item[5] * serving) / 100
            fat = (item[6] * serving) / 100
            
            lines.append(
                f"🍎 {name} ({serving}g):\n"
                f"• Calories: {calories:.1f}kcal\n"
                f"• Protein: {protein}g\n"
                f"• Carbs: {carbs}g\n"
                f"• Fat: {fat}g\n"
            )
        except IndexError:
            lines.append(f"⚠️ Couldn't format: {str(item)}")
    
    return "\n".join(lines)

def format_training_data(training_list: list) -> str:
    """Formats workout data"""
    lines = []
    for item in training_list:

        try:
            exercise = item[1]
            weight = item[2]
            reps = item[3]
            rir = item[4]
            
            lines.append(
                f"🏋️ {exercise}:\n"
                f"• Weight: {weight}kg\n"
                f"• Reps: {reps}\n"
                f"• reps in reserve: {rir}\n"
            )
        except IndexError:
            lines.append(f"⚠️ Couldn't format: {str(item)}")
    
    return "\n".join(lines)

def format_cardio(training_list: list) -> str:
    lines = []
    for item in training_list:
        try:
            name = item[1].title()
            distance = item[2]
            time = item[3]
            
            lines.append(
                f"🏋️ cardio: {name}:\n"
                f"• distance: {distance} meters\n"
                f"• time: {time} seconds\n"
                f"speed: {distance / time} m/s"
            )
        except IndexError:
            lines.append(f"⚠️ Couldn't format: {str(item)}")
    
    return "\n".join(lines)

def format_analytics(training_list: list):
    return training_list




