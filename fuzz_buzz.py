# Fuzz-Buzz problem

# accept a number from the user - input(), int()
# if that number is dividable by 3 print('Fuzz')
# if that number is dividable by 5 print('Buzz')
# if that number is dividable by 3 and 5 print('FuzzBuzz')

for i in range(3):
    num = int(input("Enter your number:"))
    if num % 3 == 0 and num % 5 == 0:
        print('FuzzBuzz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')

bin_num = bin(45)
print(bin_num)
