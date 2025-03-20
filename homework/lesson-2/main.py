## 1. Variables and Basic Data Types
my_number = 10
my_string = "Hello, Python!"
my_float = 3.14

print("Number:", my_number)
print("String:", my_string)
print("Float:", my_float)



# 2. Working with Different Data Types
#a
first_name = "Ekram"
last_name = "Alomari"
full_name = first_name + " " + last_name

print("Full name:", full_name)

#b
a = 5
b = 3
add_result = a+b
sub_result = a-b
mult_result = a*b
div_result = a/b

print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mult_result)
print("Division:", div_result)


# 3. Booleans and Comparisons
#a 
is_greater = 5>3
is_equal = 5==3
is_smaller = 5<3
print("Is greater:", is_greater)
print("Is equal:", is_equal)
print("Is smaller:", is_smaller)

#b 
'''this one I copied from solution'''

bool1= True
bool2= False
and_result = bool1 and bool2
or_result = bool1 or bool2
print("And result:", and_result)
print("Or result:", or_result)
print ("Not bool1:", not bool1)
print ("Not bool2:", not bool2)

#c
'''
1. NO pi != pi_pi because pi is a float while pi_pi is a string
2. YES pi_pi == pi_pi_pi beacause both of them are strings regardless of the " or ' used to wrap them

'''
## 4. Type checking and conversion.
#a
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"

print("pi is a", type(pi))
print("pi_pi is a", type(pi_pi))
print("pi_pi_pi is a", type(pi_pi_pi))
# print (pi_pi == pi_pi_pi)

#b
my_str = "123"
my_int = 123
my_float_converted = 12.3
print(my_str, my_int, my_float_converted)

## 5. Challenge
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print (celsius, fahrenheit)