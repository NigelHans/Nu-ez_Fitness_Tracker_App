import datetime

user_account = {}

def register_user():
    print("Register User")
    while True:
        try:
            username = input("Enter username (or leave blank to exit.): ")
            if not username:
                return
            if username in user_account:
                print("Username already exists. Please enter a new username.")
                continue
            password = input("Enter a Password (must be 8 characters or more): ")
            confirm_password = input("Confirm Password: ")
            if len(password) < 8:
                print("Password must be 8 characters or more. Please try again.")
                continue
            while password != confirm_password:
                print("Passwords do not match. Try again.")
                return register_user()
            def register_user():
                user_account[username] = {"password": password, "daily_steps": 0, "step_goal": 0, "history": [], "water_intake": 0, "diet_plan": [], "schedule_calendar": []}
            print("Registration Successful!")
            print(f'Your Username is {username} and your Password is {password}')
            return main()
        except ValueError as e:
            print(e)

def sign_in():
    print("Sign-in")
    while True:
        try:
            username = input("Enter username (or leave blank to exit.): ")
            if not username:
                return
            password = input("Enter Password: ")
            if user_account.get(username) and user_account[username]["password"] == password:
                print("Sign-in Successful")
                print("\n==== Welcome to the Fitness Tracker Application ====")
                return user_account[username]
            else:
                print("Invalid Username or Password")
                return sign_in()
        except ValueError as e:
            print(e)

def set_goal(user):
    while True:
        print("\n===== Set Workout Goal =====")
        print("Choose the type of workout goal you want to set:")
        print("1. Duration-based goal (e.g., 30 minutes of cardio)")
        print("2. Intensity-based goal (e.g., burn 500 calories)")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                duration = int(input("Enter the duration of the workout (in minutes): "))
                user['workout_goal'] = {'type': 'duration', 'duration': duration}
                print("Workout duration goal set successfully.")
                return
            elif choice == 2:
                intensity = int(input("Enter the target calorie burn (in calories): "))
                user['workout_goal'] = {'type': 'intensity', 'intensity': intensity}
                print("Workout intensity goal set successfully.")
                return
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError as e:
            print(e)

def log_activity(user, activity_type, duration):
        if activity_type.lower() in ['cycling', 'swimming', 'weightlifting']:
            if activity_type.lower() == 'cycling':
                calories_burned = duration * 10
            elif activity_type.lower() == 'swimming':
                calories_burned = duration * 12
            elif activity_type.lower() == 'weightlifting':
                calories_burned = duration * 5
            user['history'].append((datetime.date.today(), activity_type.capitalize(), duration, calories_burned))
            print("Activity logged successfully.")
        else:
            print("Invalid activity type. Please choose from cycling, swimming, or weightlifting.")

def log_steps(user, steps, duration):
    user['daily_steps'] += steps
    user['history'].append((datetime.date.today(), "Walking", duration, steps * 0.05))
    print("Steps logged successfully.")

def display_history(user):
    print("\n===== Activity History =====")
    for date, activity, duration, calories in user['history']:
        print(f"Date: {date}, Activity: {activity}, Duration: {duration} minutes, Calories Burned: {calories}")
    print(f"Total steps: {user['daily_steps']}")

def diet_plan_options(user):
    while True:
        print("\n===== Diet Plan Menu =====")
        print("1. Set Daily Calorie Goal")
        print("2. Log Meal")
        print("3. Display Daily Diet Summary")
        print("4. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                set_calorie_goal(user)
            elif choice == 2:
                log_meal(user)
            elif choice == 3:
                display_daily_diet_summary(user)
            elif choice == 4:
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError as e:
            print(e)
    
def set_calorie_goal(user):
    while True:
        try:
            calorie_goal = int(input("Enter your daily calorie goal: "))
            user['diet_plan'].append({"date": datetime.date.today(), "calorie_goal": calorie_goal, "meals": []})
            print("Daily calorie goal set successfully.")
            return
        except ValueError as e:
            print(e)

def log_meal(user):
    while True:
        try:
            meal_name = input("Enter meal name: ")
            calorie_intake = int(input("Enter calorie intake for the meal: "))
            user['diet_plan'][-1]["meals"].append({"name": meal_name, "calories": calorie_intake})
            print("Meal logged successfully.")
            return
        except ValueError as e:
            print(e)

def display_daily_diet_summary(user):
    today = datetime.date.today()
    for plan in user['diet_plan']:
        if plan['date'] == today:
            print("\n===== Daily Diet Summary =====")
            print(f"Date: {plan['date']}")
            print(f"Daily Calorie Goal: {plan['calorie_goal']} kcal")
            total_calories = sum(meal['calories'] for meal in plan['meals'])
            print(f"Total Calories Consumed: {total_calories} kcal")
            remaining_calories = plan['calorie_goal'] - total_calories
            print(f"Remaining Calories: {remaining_calories} kcal")
            print("Meals:")
            for meal in plan['meals']:
                print(f"- {meal['name']}: {meal['calories']} kcal")
            return
    print("No diet plan found for today.")

def schedule_calendar(user):
    print("\n===== Schedule Calendar =====")
    print("1. Add Event")
    print("2. View Schedule")
    print("3. Back to Main Menu")

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_event(user)
            elif choice == 2:
                view_schedule(user)
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError as e:
            print(e)

def add_event(user):
    event_date = input("Enter the date of the event (YYYY-MM-DD): ")
    event_name = input("Enter the name of the event: ")
    user['schedule_calendar'].append({"date": event_date, "name": event_name})
    print("Event added to the schedule.")

def view_schedule(user):
    if user['schedule_calendar']:
        print("\n Schedule")
        for event in user['schedule_calendar']:
            print(f"Date: {event['date']}, Event: {event['name']}")
    else:
        print("No events scheduled.")

def sign_in_options(user):
    name = input("\nEnter your name: ")
    age = int(input("\nEnter your current age: "))
    weight_kg = float(input("\nEnter your weight in kilograms: "))
    height_cm = float(input("\nEnter your height in centimeters: "))
    resting_heart_rate = float(input("\nEnter your Heart rate's BPM: "))

    while True:
        print("\n===== Fitness Tracker Menu =====")
        print("1. Set Goal")
        print("2. Add Steps")
        print("3. Display Distance")
        print("4. Track Additional Activity")
        print("5. Display Calories Burned")
        print("6. Display Summary")
        print("7. Display History")
        print("8. Calculate Heart Rate (BPM)")
        print("9. Calculate BMI")
        print("10. Diet Plan")
        print("11. Schedule Calendar")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            set_goal(user)
        elif choice == 2:
            steps = int(input("Enter the number of steps: "))
            duration = int(input("Enter the duration of the activity (in minutes): "))
            log_steps(user, steps, duration)
        elif choice == 3:
            distance = calculate_distance(user['daily_steps'])
            display_distance(name, distance)
        elif choice == 4:
            activity_type = input("Enter the type of activity (cycling/swimming/weightlifting): ")
            duration = int(input("Enter the duration of the activity (in minutes): "))
            log_activity(user, activity_type, duration)
        elif choice == 5:
            total_calories = calculate_total_calories(user['history'])
            display_calories(name, total_calories)
        elif choice == 6:
            display_summary(user)
        elif choice == 7:
            display_history(user)
        elif choice == 8:
            heart_rate = calculate_heart_rate(age, resting_heart_rate)
            display_heart_rate(name, heart_rate)
        elif choice == 9:
            bmi = calculate_bmi(weight_kg, height_cm)
            display_bmi(name, bmi)
        elif choice == 10:
            diet_plan_options(user)
        elif choice == 11:
            schedule_calendar(user)
        elif choice == 12:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

def edit_user_profile(user):
    print("\n===== Edit User Profile =====")
    print("1. Change Name")
    print("2. Update Age")
    print("3. Update Weight")
    print("4. Update Height")
    print("5. Back to Main Menu")
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                new_name = input("\nEnter your new name: ")
                user['name'] = new_name
                print("Name updated successfully.")
            elif choice == 2:
                new_age = int(input("\nEnter your new age: "))
                user['age'] = new_age
                print("Age updated successfully.")
            elif choice == 3:
                new_weight = float(input("\nEnter your new weight in kilograms: "))
                user['weight'] = new_weight
                print("Weight updated successfully.")
            elif choice == 4:
                new_height = float(input("\nEnter your new height in centimeters: "))
                user['height'] = new_height
                print("Height updated successfully.")
            elif choice == 5:
                return main()
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                print("Updated Profile:")
                print_user_profile(user)
        except ValueError as e:
            print(e)

def print_user_profile(user):
    print("\n===== User Profile =====")
    print(f"Name: {user.get('name', 'N/A')}")
    print(f"Age: {user.get('age', 'N/A')}")
    print(f"Weight: {user.get('weight', 'N/A')} kg")
    print(f"Height: {user.get('height', 'N/A')} cm")

def settings(user):
    print("\n===== Settings =====")
    print("1. Change Units of Measurement")
    print("2. Notification Preferences")
    print("3. Back to Main Menu")
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                change_units_of_measurement(user)
            elif choice == 2:
                notification_preferences(user)
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError as e:
            print(e)

def change_units_of_measurement(user):
    print("\n===== Units of Measurement =====")
    print("1. Metric (Kilometers, Kilograms)")
    print("2. Imperial (Miles, Pounds)")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user['units'] = 'metric'
                print("Units of measurement updated to Metric.")
                return
            elif choice == 2:
                user['units'] = 'imperial'
                print("Units of measurement updated to Imperial.")
                return
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError as e:
            print(e)

def notification_preferences(user):
    print("\n===== Notification Preferences =====")
    print("1. Turn On Notifications")
    print("2. Turn Off Notifications")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user['notifications'] = True
            print("Notifications turned on.")
            return
        elif choice == 2:
            user['notifications'] = False
            print("Notifications turned off.")
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

def main():
    user = None
    
    while True:
        print("\n===== Fitness Tracker Main Menu =====")
        print("1. Register User")
        print("2. Sign-In User")
        print("3. Edit User Profile")
        print("4. Settings")
        print("5. Exit")

        try:
            choice = int(input("Kindly enter the number of your choice: "))

            if choice == 1:
                register_user()
            elif choice == 2:
                user = sign_in()
                if user:
                    sign_in_options(user)
            elif choice == 3:
                if user:
                    edit_user_profile(user)
                else:
                    print("Please sign in to edit your profile.")
            elif choice == 4:
                if user:
                    settings(user)
                else:
                    print("Please sign in to access settings.")
            elif choice == 5:
                print("Exiting...")
                return
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError as e:
            print(e)

def display_distance(name, distance):
    print(f"{name}'s Distance: {distance:.2f} km")

def display_bmi(name, bmi):
    print(f"{name}'s BMI: {bmi:.2f}")

def display_calories(name, total_calories):
    print(f"{name}'s Total Calories Burned: {total_calories} kcal")

def display_heart_rate(name, heart_rate):
    print(f"{name}'s Heart Rate: {heart_rate} BPM")

def display_summary(user):
    total_steps = user['daily_steps']
    total_calories = calculate_total_calories(user['history'])
    total_distance = calculate_distance(total_steps)
    print("\n===== Summary =====")
    print(f"Total Steps: {total_steps}")
    print(f"Total Distance: {total_distance:.2f} km")
    print(f"Total Calories Burned: {total_calories}")

def calculate_distance(steps):
    distance_km = steps * 0.00075
    return distance_km

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def calculate_total_calories(history):
    total_calories = sum(calories for _, _, _, calories in history)
    return total_calories

def calculate_heart_rate(age, resting_heart_rate):
    max_heart_rate = 220 - age
    heart_rate_reserve = max_heart_rate - resting_heart_rate
    target_heart_rate = (0.5 * heart_rate_reserve) + resting_heart_rate
    return target_heart_rate

main()
