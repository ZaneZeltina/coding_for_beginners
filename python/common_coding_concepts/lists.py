"""
Python lists script
"""
# Example 1
primes = [2, 3, 5, 7, 11, 13, 17]
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

print(primes[0], rainbow[2])

rainbow[0] = "ruby"
print(rainbow)

primes.append(21)
print(primes)

print(len(primes))

# Example 2
men = "Greg","Charlie", "Jack"
women = "Danielle", "Myrtle"
people = [men, women]

print(people)
print(people[1][0])

# Example 3
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

print(c)