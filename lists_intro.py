# IDE - integrated Development Environment
# java - eclipse, IntellijIdea
# python - VScode, pycharm, VIM
#   CHAPTER 3 : INTRODUCTION TO LISTS
# print("Hello World!!")
#
# # todo: introduction to list data structure
# # todo: creating a list
students = ['john', 'mark', 'aziz', 'feruza', 105]
# # varname assign [0, 1,        2,       3   , 4 ]
# print(students)
# print(students[2])

# todo: accessing the elements in the list
# lists hold values by index, index start with 0
# print(students[0])  # prints the 1st element in the list
# print(students[3])  # 'feruza' to be printed

# reformat the file based on PEP8 rules >> CTRL + ALT + L

# Data structures: lists, tuples, dictionaries (HashMap, Hashset..)
# create, access the elements, modify, remove element from Data structure, organize
print(f"Hello, {students[1].title()}! Thank you for coming.")
# print(f"Hello, {students[4]}! Thank you for coming.")
# print("Hello, " + str(students[4]) + "! Thank you for coming.")

# TIY 3-3. create cars list, print different message for each car

# cars = ['bmw', 'nissan', 'mazda', 'honda']
# print(f"I would travel on {cars[0]}")
#
# cars = ['Honda', 'Volvo', 'BMW']
# print(f"Hello Mark! would you like to drive {cars[0]} or {cars[1]} or {cars[2]}")
# car = ['honda', 'toyota', 'ford']
# print(f"I would like to own a " + str(car[2]) + " car")

# MODIFY LISTS
cars = ['bmw', 'nissan', 'mazda', 'honda']
print(f"before: {cars}")
cars[2] = 'tesla'  # this will replace 'mazda'
print(f'after "modification": {cars}')

# ADDING ELEMENT
# appending
cars.append('lexus')  # this will add the 'lexus' to the end of the list
print(cars)

# inserting
cars.insert(2, 'toyota')  # this will insert and move all other object to right, nothing lost
print(cars)

# REMOVE FROM THE LIST
# delete by index
print(cars[5])
del cars[4]
print(f"after del {cars}")
# print(cars[5]) # you will get >> IndexError: list index out of range
#  comment the line where  your cursor is >> CTRL + /

cars.pop()  # returns the value that is being removed
print(f"after pop: {cars}")

cars.pop(2)
print(f"after pop(2): {cars}")

# delete by value
cars.remove('nissan')
print(f"after remove :{cars}")

# # TIY 3-4 and 3-5
# print(f"welcome to the dinner {guests[0]}"). Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
guests = ['D.Trump', 'Putin', 'Messi', 'CRonaldo', 'Alex Morgan']
print("================= 3-4 =========================")
print(f"welcome to the dinner {guests[0]}!")
print(f"welcome to the dinner {guests[1]}!")
print(f"welcome to the dinner {guests[2]}!")
print(f"welcome to the dinner {guests[3]}!")
print(f"welcome to the dinner {guests[4]}!")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.
# 'M.Sharapova'
guests_not_coming = []
guests_not_coming.append(guests[0])
guests[0] = 'M.Sharapova'

print("================= 3-5 =========================")
print(f"{guests[4]} sorry to hear that, please come next time.")
print(f"Guests are coming: {guests}")
print(f"Guests are NOT coming: {guests_not_coming}")
print(f"welcome to the dinner {guests[0]}!")
print(f"welcome to the dinner {guests[1]}!")
print(f"welcome to the dinner {guests[2]}!")
print(f"welcome to the dinner {guests[3]}!")
print(f"welcome to the dinner {guests[4]}!")

# Organizing your list
# temporary and permanent sorting
print(sorted(guests))  # temp sorting , sorted() works for some other data structures
sorted_guests = sorted(guests)  # sorted() - returns you the copy of the list but sorted in asc
print(sorted_guests)
print(guests)

guests.reverse()
print(f"Reversing the list: {guests}")

guests.sort()  # only works for list and does not return anything, just effects the orig list
print(f"Perm sorting with list.sort() : {guests}")
guests.sort(reverse=True)
print(f"Perm reverse (desc) sorting with list.sort() : {guests}")

# list.reverse() - reverses but not desc order
# list.sort(reverse=True) - sorts in desc order
print()
nums = [4, -10, 9, 5, 6, 1, 0, 44]
print(nums)
nums.reverse()
print(nums)
nums.sort(reverse=True)
print(nums)
# nums[8] = 100 # IndexError: list assignment index out of range
nums.insert(8, 100)
print(nums)

print(f"Number of elements in my 'nums' list :{len(nums)}")
num_elements = len(nums)
print(nums[-1])
print(nums[-5])
print(nums[-10]) # IndexError: list index out of range

# All you need to know about the LIST
# list_name = [] - creating an empty list
# list.append(newValue)
# list.insert(ind, value)
# del list[ind]
# list.remove(value)
# list.pop() - removes and returns the last element, list.pop(ind)
# list[ind] = value  - assigning a new value to existing Index
# list.sort(), list.sort(reverse=True)
# sorted(list) -  copies the list and returns sorted copy of the list
# list.reverse()
# len(list) - returns the length of your list (how big is list, i.e. number of elements)
# list[-n] - index start from the end of the list, last element is list[-1]

# HW: 3-6, 3-7
# HW TIY 3-8
