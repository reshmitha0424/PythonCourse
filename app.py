print('Reshmitha Uppala') #can be single quotes or double
#A string is executed within quotes

#This is the code to print the dog's body - to interpret how the python code works.
print('0----')
print(' ||||')
#The python code works line by line from the top

print('*' * 10) #prints 10 *
#here '*' * 10 is an expression
# - piece of code that produces a value

#VARIABLES ---------------------------------
price = 10 #when the interpreter executes this code, it will allocate some memory to store number 10 in that memory and attaches "price" label to that memory location.
#The number 10(which is now in decimal format) gets converted to binary representation, as computers understand only binary format 0s and 1s)
print(price)

price = 15 #integer
rating = 4.5 #float
name = 'Movie1' #string
is_action = True #Boolean

#******* Exercise - Variables *******
patient_name = 'John Smith'
patient_age = 20
is_new = True #to check if the patient is old or new patient


#RECEIVING INPUT ---------------------------------
your_name = input('Enter your name: ')
#The interpreter prints “What is your name?” on the terminal for the user to give their name as the input. The value that the user gives is stored in the variable called ‘name’.
print('Hi '+your_name) #+ sign is used for concatenate the strings.

#******* Exercise - Receiving input *******
your_name = input('Enter your name: ')
your_fav_color = input('Enter your favourite color: ')
print(your_name + ' likes '+ your_fav_color)




