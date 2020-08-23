# Chapter 3:
# friends = ['mark', 'john', 'jane', 400, 500]
# print(friends[-1])
#
# for b in friends:
#     print(b)
#
# # num_elements = len(friends)
# # for i in range(num_elements): # using the index
# for i in range(len(friends)): # using the index  >> this means range
#     print(f"element on index {i} is {friends[i]}")
#
# print(i)
#
# friend = 'anthony'
# for i in friend:
#     print(i)
# -------------------
"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
guests = ['mark', 'john', 'jane']

print(guests)
guests.insert(0, 'David Guetta')  # insert(index, value)
print(guests)
guests.insert(2, 'Filipp Kirkorov')
print(guests)
guests.append('Maria Kerry')
print(f"Final guests: {guests}")
print(f"We have now more space and {guests[0]} we are still waiting you for dinner!")

print("# 3-8 ****************************")
dream_places = ['Belarus', 'London', 'Bali', 'Australia', 'Italy']
print(dream_places)

print(sorted(dream_places))
print(dream_places)

print(sorted(dream_places, reverse=True))
print(dream_places)

dream_places.reverse()  # reverse() puts your list in reverse order, not desc order
print(dream_places)

dream_places.sort()  # sort() order your list in ASC order
print(dream_places)

dream_places.sort(reverse=True)  # sort() order your list in DESC order
print(dream_places)
