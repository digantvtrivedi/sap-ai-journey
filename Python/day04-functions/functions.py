def greet(name):
    print(f"Hello {name}!")


greet("Digant")
greet("Reeva")
greet("AI Engineer")

def add(a, b):
    return a + b

result = add(1, 9)
print(result)

def years_to_retirement(current_age):
    if current_age >= 60:
        return "Already Retired"
    else:
        years_left = 60 - current_age
        return years_left

retirement_years = years_to_retirement(61)
print(retirement_years)