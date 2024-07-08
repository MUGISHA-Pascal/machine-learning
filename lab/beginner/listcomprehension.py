# filtering even numbers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=[num for num in numbers  if num%2==0]
# print(even_numbers)

# transformations 
# square each number in a list
# numbers=[1,2,4,5,6,7,8,9,10]
# sq_numbers=[num**2 for num in numbers]
# print(sq_numbers)

# generation
# first 10 squared numbers
# sq=[num**2 for num in range(1,11)]
# print(sq)

# combining filtering and transformation
# even_sq=[num**2 for num in range(1,11) if num%2==0]
# print(even_sq)

# nested list comprehension
# generating a pair 
# pairs=[(i,j) for i in range(1,4) for j in range(1,4)]
# print(pairs)

# flattening a nested list
# nested_list=[[1,2,3],[4,5,6],[7,8,9]]
# oned=[num for sublist in nested_list for num in sublist]
# print(oned)

# conditional assignment
# numbers=[1,2,3,-1,-2,-3]
# nonzero=[num if num>0 else 0 for num in numbers]
# print(nonzero)

# generating a list of strings
# names=["mugisha","pascal","daddy"]
# listofstrings=[f"hello {name}" for name in names]
# print(listofstrings)

# generating a list of vowels in a string
# string="pasu,ical"
# vowels=[char for char in string  if char in ["a","e","u","i","o"]]
# print(vowels)

# capitaling the first letter in a string
# string="this is a string"
# capitalized=[stri.capitalize() for stri in string.split(" ")]
# print(" ".join(capitalized))

# list for multiplication table lists
# multilist=[[num*multp  for num in range(1,11) ] for multp in range(1,11)]
# print(multilist)