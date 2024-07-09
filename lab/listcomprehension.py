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

# generating a dictionary from a list
# listo=[1,2,4,5,7]
# dicto={num for num in listo}
# print(dicto)

# generating a key value dictionary
# keyvalue=[("key","value"),("key2","value2"),("key3","value3")]
# keydict={key : value for key,value in keyvalue}
# print(keydict)

# flattening a list into a single list
# twodlist=[[1,2,3],[4,5,6]]
# onedlist=[num for sublist in twodlist for num in sublist]
# print(onedlist)

# Filter based on multiple conditions(even>5)
# numbers=[1,2,3,4,5,6,7,8,9,10]
# filtered=[num for num in numbers if num % 2 ==0 and num >5]
# print(filtered)

# Prime number generation
# def isprime(n):
#     return n > 1 and all( n % i != 0 for i in range(2,int(n ** 0.5)+1))
# limit=10
# primenumbers=[num for num in range(1,limit+1) if isprime(num)]

# products generation
# products = [
#     {"name": "Shirt", "price": 15.00, "in_stock": True},
#     {"name": "Hat", "price": 7.50, "in_stock": False},
#     {"name": "Socks", "price": 8.00, "in_stock": True},
#     {"name": "sweater", "price": 20.00, "in_stock": True},
# ]

# newlist=[objecti for objecti in products if objecti["name"].startswith("S") and objecti["price"]>10 and objecti["in_stock"]==True]
# print(newlist)

# conditional dictionary generation
# words = ["listen", "silent", "boat", "table", "eat", "ate"]
# casedict={key:key.capitalize() for key in words }

# anagram program
# words = ["listen", "silent", "boat", "table", "eat", "ate"]
# disowords=["listen","boat","eat"]
# def sort_word(w):
#     return " ".join(sorted(w)) 
# anagram_group={key:[word for word in words if sorted(word) == sorted(key)] for key in disowords  }
# print(anagram_group)