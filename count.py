# https://docs.python.org/3/library/configparser.html
import configparser

config = configparser.ConfigParser()

# intialize count variables
number_of_letters = 0
instance_of_numbers = 0

# read mydefaults.ini file using read method
config.read("./mydefaults.ini")
for section in config.sections():
    for char in section:
        if char.isalpha():
            number_of_letters += 1


# iterate through each key(str), value(str) in configparser object and only iterate each count variable
# if it is a number or letter
for key, value in config.items("Setup"):
    for char in key:
        if char.isalpha():
            number_of_letters += 1
        if char.isdigit():
            instance_of_numbers += 1
    for char in value:
        if char.isalpha():
            number_of_letters += 1
        if char.isdigit():
            instance_of_numbers += 1

# write count vairables to output.txt file
with open("output.txt", "w") as file:
    file.write(f"Number of letters [a-z,A-Z]: {instance_of_numbers}\n")
    file.write(f"Instance of numbers [0-9]: {number_of_letters}\n")
