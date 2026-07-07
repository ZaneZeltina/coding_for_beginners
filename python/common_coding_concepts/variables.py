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

"""
Working with number data type
"""
# Starting with sweets in my cupboard
sweets_in_my_cupboard = 50
# Add number of eaten sweets
eaten_sweets = 20
# Calculate remaining sweets in my cupboard
sweets_in_my_cupboard -= eaten_sweets
# Show remaining sweets in my cupboard to the user UI/Console
print(sweets_in_my_cupboard)

"""
Another example with number and float data type
"""
# Starting with money in my wallet
money_in_my_wallet = 40
# Show money in my wallet to the user UI/Console
print(money_in_my_wallet)
# Net price of sweets
sweets_price = 7.50
# Calculating tax
sales_tax = 0.2 * sweets_price
# Calculating gross price (adding tax to the net price of sweets)
sweets_price += sales_tax
# Updating money in my wallet after buying sweets
money_in_my_wallet -= sweets_price
# Show remaining money in my wallet to the user UI/Console
print(money_in_my_wallet)