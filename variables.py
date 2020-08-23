## Data types : string
print("welcome back!")
# fstring
msg = "Welcome back to "
language = "Python"
msg_with_lan = msg + language
print(msg_with_lan)
# Welcome back to Python
print(msg + language)
# Welcome back to Python
print(msg + language + " continue with 'string'.")
# Welcome back to Python continue with 'string'.
print(f"{msg}{language} continue with 'string'.")
# Welcome back to Python continue with 'string'.
print(f"the sume of 25 and 700 is : {25+700}")
# the sume of 25 and 700 is : 725
help(print)
# Help on built-in function print in module builtins:
#
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

n = 4567
type(n)
# <class 'int'>
### Data types: string(str), integer (int), boolean(bool)
###  float(float) - numbers with decimals >> 45.788
status = True
type(status)
# <class 'bool'>
status = "True"
type(status)
# <class 'str'>
# status = true
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined
status = False
type(status)
# <class 'bool'>
price = 100.99
type(price)
# <class 'float'>
############## string ###################
msg = "john doe"
msg.title()
'John Doe'
msg = "john doe hello world"
msg.title()
'John Doe Hello World'
## str.title() - converts to titlecase
## str.upper() - converts the str to upper case
### str.lower() - converts the str to lower case
msg.title()
'John Doe Hello World'
msg.upper()
'JOHN DOE HELLO WORLD'
msg.lower()
'john doe hello world'
print(f"message : {msg.title()}!!!!")
# message : John Doe Hello World!!!!
msg
'john doe hello world'
#### whitespace : space, enter, tabs, non printable characters
print(f"\tmessage : {msg.title()}!!!!")
        # message : John Doe Hello World!!!!
print(f"\tmessage : \n{msg.title()}!!!!")
        # message :
# John Doe Hello World!!!!
print(f"\tmessage : \n\t{msg.title()}!!!!")
        # message :
        # John Doe Hello World!!!!
msg = '   john doe           '
msg
'   john doe           '
msg.strip()
'john doe'
msg.lstrip()
'john doe           '
msg.rstrip()
'   john doe'
msg = '   john                 doe           '
msg.strip()
'john                 doe'
### str.split('delimeter')
### it will split the string based on delimeter
full_name = 'john,doe'
full_name.split(',')
['john', 'doe']
full_name = 'john/doe'
full_name.split('/')
['john', 'doe']
full_name = 'john/doe/45679'
full_name.split('/')
['john', 'doe', '45679']
name = 'Erik'
print(f"Hello {name}, would you like to learn Python todat?")
# Hello Erik, would you like to learn Python todat?
name = 'erik'
print(f"Hello {name.title()}, would you like to learn Python todat?")
# Hello Erik, would you like to learn Python todat?
print('\tAlbert Einstein once said, ' + '"A person who never made a \n\tmistake never tried anything new."\n')
        # Albert Einstein once said, "A person who never made a
        # mistake never tried anything new."

##### Numbers
456+788
1244
25*1000
25000
456-56
400
700/7
100.0
# % modulo - remainder after division
# num**exp , 3**2 = 3*3, 3**4 = 3*3*3*3
# // - division floor , 10//4 = 2, 11//5 = 2, 25//12=2
# a = b*f + r >> a//b = f; a%b = r
45666
45666
num = 45666
lnum = num%10
lnum
6
### TypeError from python
msg
'   john                 doe           '
age = 25
print("I am "+ age +" years old")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
print("I am "+ str(age) +" years old")
# I am 25 years old
age = '25'
age = age + 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
new_age = age + 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
new_age = 5 + age
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
new_age = 5 + int(age)
new_age
30
age
'25'
int(age)
25
age = 5 + int(age)
age
30
age
30
age = age + 25
age
55
nage = nage + 10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'nage' is not defined
nage = 0
nage = nage + 10
nage
10
## methods = function : lines of code for certain purpose, with proper name, that are built-in with python (comes inside python package downloaded)
### Methods for string: strip(), lower(), title(), upper(), str()
### Methods for number: int(), float()
### Arithmetic operations with numbers: +, -, *, /, %, //, **