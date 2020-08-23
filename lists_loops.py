# Chapter 4: Working with LISTS
states = ['New York', 'New Jersey', 'Connecticut', 'California']
# Loops - within the loops you create repetitive actions

# for variable in list_of_elements:
#     repetitive code here

# for state in states:
#     print(f"Welcome to {state}!!")
#     print(f"Welcome to {state}!!")
# pass # do nothing

# Things to Remember while working with LOOPS
#  colon at the end of 'for' line
#  'in' in the 'for' line
#  give any name to a variable and use that variable inside the for loop code
#  lines of code that belongs to for loop (repetitive code) must be indented
#  Always check your indentation

# states >> 4 members >>
#     >> 1st loop/round >> state = 'New York'   -- python does this
#     >> print(f"Welcome to {state}!!")         -- we will write this code
#     >>> Welcome to New York!!                 -- this is execution

#     >> 2nd loop/round >> state = 'New Jersey'
#     >> print(f"Welcome to {state}!!")
#     >>> Welcome to New Jersey!!

#     >> 2nd loop/round >> state = 'Connecticut'
#     >> print(f"Welcome to {state}!!")  --- this code we will write
#     >>> Welcome to Connecticut!!

# print(states)
# # Pycharm: refactoring >> Shift + f6
#
# # print(state)  # outside of the scope of variable
# # SCOPE
# for state in states:
#     print(f"Welcome to {state.upper()}!!")
#
# print(f"Enjoy your trip!!") # outside of loop, independent from loop
# print(state)  # Incorrect : outside of the scope of variable
# print()
# # TIY 4-1 Pizza exercise
# pizzas = ['pepperoni', 'four cheese', 'salami', 'mashrooms']
# for pizza in pizzas:
#     print(f"I really love {pizza}!")
#
# print()
# pizzas = ["cheese", "artichoke", "mashroom"]
# for pizza in pizzas:
#     print(pizza)
#     print(f"I like this type of pizza {pizza}!!!")
# print("I really love pizza")

# HW 4-2

# Marking Numerical List
for num in range(5):  # from 0 to 4
    print(f"My current number from range(5): {num}")

for num in range(3, 6):  # from 3 to 5
    print(f"My current number from range(3, 6): {num}")

# list(object) - mutable >> [4, 6, 12]
# tuple -   (4, 6, 12) - immutable
friends = list()
students = []

nums = list(range(5))  # 1. range() >> 0 1 2 3     2. list() >> [0,1,2,3,4]     3. numbers = [0,1,2,3,4]
print(nums)

# print squares of numbers from 5 to 12
squares = []  # squares = list()
for num in range(5, 13):
    num_sqr = num ** 2
    # squares.insert(-1, num_sqr)
    squares.append(num_sqr)
    # print(num_sqr)
    # print(squares)
print(squares)

squares = list()  # resetting the list to empty list
for num in range(5, 13):
    squares.append(num ** 2)
print(squares)

nums = [5, 78, 456, 127, 230, 6, 5]
# min(list) , max(list), sum(list)
print(f"Min number from numbers :{min(nums)}")
print(f"Max number from numbers :{max(nums)}")
print(f"Sum number from numbers :{sum(nums)}")

# list comprehensions

squares = []
for num in range(5, 14, 2):
    squares.append(num ** 2)

# FYI
# squares = list(num ** 2 for num in range(5, 14))
squares = [num ** 2 for num in range(5, 14, 2)]
print(squares)

print("# TIY 4-5")
# for num in range(1, 1000001):
#     pass
#     # code to create a list
# print(min(num))
# print(max(num))
# print(sum(num))
# print(sum(num) / len(num))

nums = list(range(1, 1000001))
print(f"Min number is: {min(nums)}")
print(f"Max number is: {max(nums)}")
print(f"Sum number is: {sum(nums)}")

# Slicing the list
name = "John Doe"
print(name[5:])  # >>> Doe

numbers = [5, 78, 456, 127, 230, 6, 5]
print(numbers[:3])  # indexes >> 0, 1, 2
print(numbers[0:3])

print(numbers[3:])  # from 3rd index to end of the list
print(numbers[1:-2])  # from 1st index(second element) to third from the end

new_numbers = numbers  # this is linking the numbers_copy to numbers list
# if numbers is modified numbers_copy will effected
numbers_copy = numbers[:]  # copying the list to a new list

print("# copying the lists example")
print(numbers, new_numbers, numbers_copy)
numbers.append(5555)
print(numbers, new_numbers, numbers_copy)

for num in numbers[3:]:
    print(num)

# HW 4-2
# HW 4-6, 4-7, 4-8, 4-9
# HW 4-10, 4-11, 4-12


add_numbers = [1, 25, 350, 550, 750, 1000000]
print(f"Min number from numbers :{min(add_numbers)}")
print(f"Max number from numbers :{max(add_numbers)}")
# why when you use (max function) python see last numbers?
print(f"Sum number from numbers :{sum(add_numbers)}")



