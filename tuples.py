# tuples are used to store multiple items in a single variable
# tuples are not immutable unlike list you can't add to a tuples list you can only check for the index 
# tuples are separated by commas
tuple1 = ("Stribgs", 1, 2.78, True)
 # print(tuple1)

tuple2 = "meat", "bone"
 #print(type(tuple2))
tuple3 = "pond"
 # print(type(tuple3))

 # count
tuple4 = ("Amaka", "Seun", "Musa", "Musa", "Chiamaka", "Amaka")
 # print(tuple4.count("Amaka"))

 # if tuple4.count("seun") >= 2:
   # print("We have more that one seun in class")
 # else:
    #    print("We have only one seun in class")

    # index
 # print(tuple4.index("Chiamaka")) 

 #Nested Tuples
nested_tuples = ("Boy", ("John", "Greg", "Chief"), "Girl", ("Anna", "joy", "Hillary"))
#print(nested_tuples)

print(tuple4[2:])