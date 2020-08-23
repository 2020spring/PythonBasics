# 08/15/2020 IF CONDITIONS

cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
# for car in cars:
#     if car == 'bmw':  # car == 'bmw' >> expression to return True or False
#         print(car.upper())  # if expression returns True, else case is skipped
#     else:
#         print(car.title())  # if expression returns False, if case is skipped
#
# # if expression:
# #     code to execute when expression is True
# # elif expression2:
# #     code to execute when expression2 is True
# # else:
# #     code to execute for all other cases
#
# is_bmw_listed = ('bmw' in cars)
# print(is_bmw_listed)
# print('bmw' in cars)
#
# if ('bmw5' not in cars):
#     cars.append('bmw5')
# print(cars)
# # ----
# print()
# for car in cars:
#     if 'bmwx5' != car.lower():
#         print(f"{car} is not bmwx5")
#
# print(cars)
#
# status = False
# if status:
#     print('it is true')
# else:
#     print('it is not true')

# Multiple condition
age = int('25')  # , if age> 20
states_17 = ['NY', 'CA', 'NC', 'VA', 'CT']
states_16 = ['NJ', 'WA', 'MA', 'TX', 'VT']

for i in range(3):
    print("************* DL check starts *************************")
    age = int(input("Enter your age: "))
    state = input("Enter your State: ").upper()
    if age >= 16 and state in states_16:  # True and True >> True, True and False >> False
        print(f'You are eligible to apply for Driving Licence in following states: \n{states_16}')
        print("Available cars in these states: ")
        for car in cars[:2]:
            print(f"\t{car}")

    elif age >= 17 and state in states_17:  # True and True >> true
        print(f'You are eligible to apply for Driving Licence in in following states: \n{states_17}')
        print("Available cars in these states: ")
        for car in cars[2:]:
            print(f"\t{car}")
    else:
        # diff = 17 - age
        # print(f'You will be eligible to apply for DL in {diff} years.')
        print(f'You are not eligible to apply for DL yet.')

print("******************** Program ends *******************************")
