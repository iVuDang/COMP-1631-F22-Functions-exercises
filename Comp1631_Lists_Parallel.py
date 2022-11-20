
# PARALLEL LISTS - Find oldest person, with list of names, and list of ages. 

ages = [19,18,20]
names = ["Aaliya", 'Farah', 'Sada']

oldest_age = max(ages)
position_oldest_names = ages.index(oldest_age)

oldest_name = names[position_oldest_names] # List[index position in the list]


print(oldest_name)


#-------------------------------------------------------------------------------

# PRINTING LISTS WITH * AND FOR LOOP

this_list = [ 4, 4.0, "4", 'four', [0,1,2,3], True ]


print ("1. print the contents of a list in a single line with space:")
print (*this_list)

print ("--------------------")


print("2. print the contents of a list in a single line with space, with commas:")
print (*this_list, sep = ",")

print ("--------------------")


print("3. printing lists in new line using *:")
print (*this_list, sep="\n")

print ("--------------------")


print("4. printing lists in new line using for loop:")
for item in this_list:
  print(item)
  
print ("--------------------")


print("5. printing lists in new line using for loop with range:")
for i in range(0, len(this_list)):
  print(this_list[i])

print ("--------------------")



#-------------------------------------------------------------------------------

odd_nums = [1, 3, 5, 7]


print ("Re-assign individual item in list")
odd_nums[0] = 55

print(odd_nums)



print ("--------------------")


print ("Retrieving individual item from list")
value_at_zero = odd_nums[0]

print(value_at_zero)



print ("--------------------")


print ("Calculate with items in list")
print (2 * odd_nums [2] + value_at_zero)



print ("--------------------")