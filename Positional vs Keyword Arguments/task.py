# Functions with input
def life_in_weeks(current_age):
    weeks = 52
    amount_of_weeks_90 = weeks * 90
    weeks_already_lived = current_age * weeks
    weeks_left = amount_of_weeks_90 - weeks_already_lived
    print(f"You have {weeks_left} weeks left.")


life_in_weeks(32)


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
