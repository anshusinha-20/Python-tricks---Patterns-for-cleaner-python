## 2.1 Covering your A** with assertions

# """function to apply discount"""
# def applyDiscount(product, discount):
#     """holds the discounted price"""
#     price = int(product["price"] * (1 - discount))
#     """makes sure that the price is not lower than 0 and not higher than the original price"""
#     assert 0 <= price <= product["price"]
#     """returns the discounted price"""
#     return price

# """shoes dictionary"""
# shoes = {"name": "Fancy Shoes", "price": 15000}
# """discounted price is printed"""
# print(applyDiscount(shoes, 0.25))

# """passing some invalid discount rates, like 200%"""
# print(applyDiscount(shoes, 2))

# """
# Note: 
# 1. Never use assertions for data validations
# 2. Python's assert statement is a debugging aid that tests for a condition as an
#     internal self-check in your program
# 3. Asserts should only be used to check for bugs, they are not a mechanism
#     for handling run-time errors
# 4. Asserts can globally be disabled with an interpreter setting
# """

#####

## Complacent comma placement

# """defining list, dict or set with spread out technique"""
# name = [
#     "Anshu",
#     "Sahil",
#     "Jane" # concatenates JaneAmy,when no commas
#     "Amy"
# ]

# print(name)

# """useful way to write long strings, splitted across multiple lines of strings"""
# myStr = ("This is what I intended to be, "
#          "a Python programemr.")
# print(myStr)

# """Here's the final trick"""
# name = [
#     "Jane",
#     "Austin",
#     "Sam",
# ]

# print(name)