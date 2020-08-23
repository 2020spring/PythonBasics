# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt.'
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississippi': 'usa', 'thames': 'uk'}

# • Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt.'
# The KEY runs through VALUE
for river, country in rivers.items():
    # if country == 'usa' or country == 'uk':
    if country in ['usa', 'uk']:
        print(f"The {river.title()} runs through {country.upper()}.")
    else:
        print(f"The {river.title()} runs through {country.title()}.")

# • Use a loop to print the name of each river included in the dictionary.
print('Rivers are: ')
for river in rivers.keys():
    print('\t', river.title(), end=" | ")

# • Use a loop to print the name of each country included in the dictionary.
print('\nCountries are: ')
for country in sorted(rivers.values(), reverse=True):
    if country in ['usa', 'uk']:
        print('\t', country.upper(), end=" | ")
    else:
        print('\t', country.title(), end=" | ")
# print('a', end=" | ")
# for r, c in rivers.items():
#     print(rivers[r]) # value
#     print(r)  # key
#     print(c)  # value


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

print("\n\n************** 6-11. Cities: **********************")
cities = {'new york': {'country': 'USA', 'population': 8.4, 'fact': 'Big Apple'},
          'istanbul': {'country': 'Turkey', 'population': 15.52, 'fact': 'Constantinople'},
          'tashkent': {'country': 'Uzbekistan', 'population': 2.5, 'fact': 'Stone City'},
          'moscow': {'country': 'Russia', 'population': 12.53, 'fact': 'Kremlin'}
          }
# "CITY is very beautiful city in COUNTRY. It has POPULATION population and the city is also known as FACT"

for city, info in cities.items():
    # print(city)
    # print(info)
    print(f"{city.title()} is very beautiful city in {info['country']}. "
          f"It has {info['population']} mln population and the city is also known as {info['fact']}.")

# HW:
# print multiplication table 1-10
for i in range(2):
    input('enter your input')