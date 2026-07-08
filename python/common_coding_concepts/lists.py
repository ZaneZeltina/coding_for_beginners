"""
Python lists script
V.1.0
"""

# Set up a list of numbers
primes = [2, 3, 5, 7, 11, 13, 17]
# Set up a list of colors in the rainbow (String data type)
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# Print out index 0 value from primes list and index 2 value from rainbow list
print(primes[0], rainbow[2])
# Set a new value for index 0 in the rainbow list
rainbow[0] = "ruby"
# Print out the updated rainbow list
print(rainbow)
# Add a number 21 to the end of the primes list
primes.append(21)
# Print out the updated primes list
print(primes)
# Print out the length of the primes list
print(len(primes))

"""
Working with Dual lists
"""

# Set up two lists of mens and womens names
men = "Greg","Charlie", "Jack"
women = "Danielle", "Myrtle"
# Combine the two lists into a list of lists
people = [men, women]
# Print out the list of lists
print(people)
# Print out the first name in the second list of the list of lists
print(people[1][0])

"""
Combine two lists into a new list
"""
# Set up two lists of numbers
a = [1, 2, 3]
b = [4, 5, 6]
# Combine the two lists into a new list using concatenation
c = a + b
# Print out the new combined list
print(c)