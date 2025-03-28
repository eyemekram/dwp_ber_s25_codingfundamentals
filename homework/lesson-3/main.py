# 1. Basic Arithmetic Operations

print ("Assign value to x ")
x = int (input ()) # Convert input to integer

print ("Assign value to y ")
y = int (input ()) # Convert input to integer

print ("x = " + str(x))
print ("y = " + str (y))
print ("x + y = " + str (x + y))
print ("x - y = " + str (x - y))
print ("x * y = " + str (x * y))
print ("x / y = " + str (x/y))



# 2. Modulus and Exponentiation
print ("type any number ")
any_number = int (input())
print ( "any_number = " + str (any_number))
print ( "Remainder when devided by 3 = " + str(any_number % 3))
print ( "number raised to power 2 = " + str (any_number ** 2))



# 3. Odd or Even
print ("choose a random number, I will tel you if it's odd or even")
number = int(input())
print ("The number is:" + str(number))

if number % 2 == 0 :
    print ("The number is even")
    
else:
     print ("The number is odd")

#TODO: add two numbers



# 4. Compare Two Numbers

print ("Welcome to the comparing number program!")

print("write the first number")
first_number = int(input ())

print("write the second number")
second_number = int(input ())

if first_number > second_number :
    print ("The first number is greater than the second")

elif first_number < second_number :
    print ("The second number is greater than the first")

elif first_number == second_number :
    print ("The two numbers are equal")



# 5. Print Numbers 1 to 10

print ("I am a smart computer, I can count to 10!")
for number in range (1, 11) :
    print (number)

# 6. Multiplication Table

print("write any number and I will  give you multiplication table for it")
chosen_number = int(input())
something = 1
while something <= 10 :
    print(f"{chosen_number} * {something} = {chosen_number * something}")
    something += 1

