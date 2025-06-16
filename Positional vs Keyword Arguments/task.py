# Functions with input
# def life_in_weeks(current_age):
#     weeks = 52
#     amount_of_weeks_90 = weeks * 90
#     weeks_already_lived = current_age * weeks
#     weeks_left = amount_of_weeks_90 - weeks_already_lived
#     print(f"You have {weeks_left} weeks left.")
#
#
# life_in_weeks(32)

# def greet(name, location):
#     print(f"Hello {name}")
#     print(f"You live in {location}")
#
#
# greet(location="Ottawa", name="Jack Bauer")

def calculate_love_score(name_1, name_2):
    check_true = "true"
    check_love = "love"
    true_score = 0
    love_score = 0

    couple = name_1.lower() + name_2.lower()

    for char in couple:
        if char in check_true:
            true_score += 1
        if char in check_love:
            love_score += 1

    true_love_score = str(true_score) + str(love_score)
    print(true_love_score)

    return true_love_score


calculate_love_score("Kanye West", "Kim Kardashian")