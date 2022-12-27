"""
BUILT-IN FUNCTIONS IN PYTHON

abs() - returns the absolute value of a number
len() - Returns the length of items of an object
max() - returns the largest item in an iterable
min() - returns the smallest item in an iterable
join() - takes all items in an iterable and joins them into one string
print() - display objects
range() - returns a sequence of number starting from the given start integer to the stop integer
round() - returns a float that is closest to the multiple of 10
floor() - rounds a number down to the nearest integer
ceil() - rounds a number up to the nearest integer
input() - allows user to input a value or allows user to provide a response
"""
# abs function
# this function takes away the negative sign of a number while numbers without negative sign are not affected
#print(abs(-10))
#speed of a vehicle
d = -10.2
t = 2.0
s = abs(d) // abs(t)
#print(s)

#LEN
name = ["i", "am", "a", "boy"]
#print(len(name))

#INPUT
#question = input("What is your name? ")
#print(question)

#MAX
#numbers = (1, 2, 3, 90, 7, 56, 98)
#print(min(numbers))

#JOIN
#sentences = ("Adegbite", "AlAreef", "Ayomipo")
#joined = " ".join(sentences)
#print(joined)

#RANGE(#start), #stop, #steps
x = range(10)
for number in x:
    print(number)

#   ROUND
#print(round(10.8993, 2))

