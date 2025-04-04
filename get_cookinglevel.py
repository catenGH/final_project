'''
This is a function to take the amount of time a user has on average to cook and turn it into a cooking level. We can use this to catagorize recipes. 
'''
#This function can be used both for getting avrg cooking time from user, as well as catagorizing recipes into levels based on total prep time.
#Time is in minutes, and these can be adjusted later if we want. Time is an int.
def get_cooklevel(time):
    if time <= 60:
        cooklevel = "beginner"
    elif time <= 120:
        cooklevel = "intermediate"
    else: 
        cooklevel = "expert"
    return cooklevel

#Example usage: A recipe has a 50 min total prep time.
cook_level = get_cooklevel(50)
print(cook_level)