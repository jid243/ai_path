# This program says hello and asks for my name

print('Hello world!')

print('What is your name?') #asks for their name
myName = input() # waits for user input
print('It is good to meet you, ' +myName)
print('The length of your name is:')
print(len(myName)) #takes a string argument and calculated the length of the string

print('What is your age?') #asks for their age
myAge = input()
print('You will be ' +str(int(myAge) + 1) + ' in a year.') #str converts int into a string so it can be added to the sentence as a word
