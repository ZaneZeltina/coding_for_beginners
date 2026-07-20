"""
Write simple Python code to demonstrate the use of variables and basic data types
"""
# Basic data types in Python
my_integer_variable = 42
my_float_variable = 3.14
my_string_variable = "Hello, World!"
my_boolean_variable = False
# Show all data types to the user UI/Console
print(my_integer_variable, my_float_variable, my_string_variable, my_boolean_variable)

# Example 2
sweets_in_my_cupboard = 50
eaten_sweets = 20
sweets_in_my_cupboard -= eaten_sweets
print(sweets_in_my_cupboard)

# Example 3
money_in_my_wallet = 40
print(money_in_my_wallet)
sweets_price = 7.50
sales_tax = 0.2 * sweets_price
sweets_price += sales_tax
money_in_my_wallet -= sweets_price
print(money_in_my_wallet)