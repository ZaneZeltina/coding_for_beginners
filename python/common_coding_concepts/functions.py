"""
Write a simple basic Python functions script
"""
# Example 1
def hello_world():
    print("Hello World!")

hello_world()

# Example 2
def say_hello(name):
    print("Hello " + name + "!")

say_hello("Zane")

# Example 3
def hi_message(name):
    print("Hi, " + name + "!")

person = "Zane"

hi_message(person)

# Example 4
def greet_message(name):
    greeting = "Hello, " + name + "!"
    return greeting

person = "Zane"

message = greet_message(person)
print(message)