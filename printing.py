"""
This code is written to refresh my memory after abandoning Python for almost 4
months! I hate having to start from the beginning but I am determined to be a
very great Python programmer.
This code is also a great way for beginners to quickly master Python basics.

Samuel A. Olubiyo
01/09/2021
"""

print("Hello World")  # Displays 'Hello World'
print("Good Bye World...")  # Displays 'Good Bye World'
print("\nIt all starts with printing Hello World and shit.")  # '\n' Prints on a new line
print("I know all these things! If not that my laptop got spoilt and I have to start again!")

# Variables

my_name = "Samuel A. Olubiyo"
my_age = 23
my_weight = 60
my_height = 6.2
my_relationship_status = "Single"
star_sign = "Cancer"

tots = my_height + my_weight + my_age  # Adding the contents of the variables

# F- Printing

print(f"\nMy name is {my_name}, I am {my_age} years old, I am also {my_relationship_status} right now, "
      f"I am a {star_sign}.")

# Maths

chickens = 4 + 5 + 11 + 16
goats = 200
dragons = 1
unicorns = chickens / dragons
pheonixes = chickens * goats / dragons
tots_animals = chickens + goats + dragons + pheonixes
print(f"In my farm I have {chickens} chickens, {goats} goats, {dragons} dragons, and {unicorns} unicorns.")
print(f"The farm is blessed with {pheonixes} phoenixes!")
print(f"There are {tots_animals} in my farm all together!")

# More Variables and Printing

joke = "Ha, I ate a mango!"
joke_eval = "Is the joke funny? {}"  # The parenthesis is important or else the test for the boolean will not work
funny = False

print(joke_eval.format(funny))  # Test for the Boolean

# More printing

end1 = "l"
end2 = "o"
end3 = "r"
end4 = "d"
end = " "
end5 = "s"
end6 = "a"
end7 = "m"

print(end1 + end2 + end3 + end4 + end + end5 + end6 + end7)

print(f"When you add my age, height and weight, you get a unique magical number {tots}!")

# Complicated String Formatting
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "A song about fear,",
    "when in darkness,",
    "snakes hisses,",
    "cats meows, terrible poem!"
))

# Printing the Months
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug\nsep\noct\nnov\ndec"
print(months)

print("I am 6'2\" tall!")
print("I am 6\'2 " "tall")

# Other Printing
lord = "\tI am Lord Sam"
print(lord)
split = "I am a\nSage"
print(split)
my_list = """
Here is my List:
\t* Learn Python
\t* Build a Game
\t* Make Tons of Money
\t* Get girl\nof my \tdreams
"""
print(my_list)

end_message = """
\tI really refreshed my memory with these printing exercises, 
I will love to refresh more of my memory,
\\Success is the goal.\\
"""

print(end_message)
