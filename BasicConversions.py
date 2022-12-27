# CONVERSION FROM PYTHON TUPLE TO LISTS, DICTIONARIES, STRINGS, ARRAY AND FROM LISTS NTO TUPLES

#CONVERSION FROM TUPLES TO LIST


My_tuple = (20, 40, 60, 80)
convert_to_list = list((My_tuple))
#print(convert_to_list)
#print(type(convert_to_list))
#print(type(My_tuple))


#CONVERSION FROM TUPLE TO DICTIONARY, NOTE WHEN CONVERTING FROM A TUPLE TO A DICTIONARY, YOUR DICTIONARY MUST HAVE A KEY AND A VALUE


Ayo_tuple = ((12, "AlAmeen's age"), (16, "AlAreef's age"), (18, "Aisha's age"), (40, "Momma's age"))

convert_to_dictionary = dict((Ayo_tuple))
#print(convert_to_dictionary)

#CONVERSION FROM TUPLES TO STRING


# you make use of the join method to convert from tuples to string in python, to use the join method, you create an empty file ending with .join followed by the tuple name see an example below
Alareef_tuple = ("I", "am", "a", "Programmer")
my_string = " ".join(Alareef_tuple)
#print(my_string)
Name_tuple = ("A", "L", "A", "R", "E", "E", "F")
name_string = " ".join(Name_tuple)
#print(name_string,"\n")



# CONVERSION FROM PYTHON TUPLE TO ARRAY
no_tuple = (10, 400, 900)
convert_array = list(no_tuple)
print(convert_array)

list1 = [ 10, 20, 30, 40, 50]

list_tuple = tuple(list1)
print(list_tuple)