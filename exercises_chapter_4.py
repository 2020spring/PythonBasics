# Chapter 4
"""
exercises_chapter_3.py
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.
"""

pizzas = ['Mozzarella', 'Regular', 'Pepperoni', 'Chicken buffulo']
# friend_pizzas = pizzas.copy()
friend_pizzas = pizzas[:]
# friend_pizzas = pizzas
# • Add a new pizza to the original list.
pizzas.append('Vegan')
# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Pineapple')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")

pizzas.count()
