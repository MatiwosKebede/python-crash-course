#In python there are several removing method and keyword such as del keyword, remove() and pop().

#del is a keyword in python that used to delete specific or full list of the list, it is also used to delete variable.
#e.g using del
Fashion_Brands = ["Puma", "Nike", "Jordan"]
print(Fashion_Brands) # Displaying the orginal list of Fashion_Brands.

del Fashion_Brands[0] # Removing item thgitat found in the first position or 0 index.
print(Fashion_Brands) # Displaying the list after some item is removed.

#remove method in python used to removing by searching the value of the item from the list, but only delete the first value, it is not use index.
#e.g using remove()

Continent_lists = ["Africa", "Asia", "Europea", "North America", "South America", "Antractica"]
print(Continent_lists) # Displaying the orginal lists.

Continent_lists.remove("Antractica")
print(Continent_lists) # Display the lists after the string called Antarctica is removed.

#pop method in python,pop is a method used to remove item from the list by defult its remove the top value which is end the value the list and return the value that removed by them, pop method windly used in the concept of stack.
#e.g removing item form the list and catching value of removed index.

planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupter", "Urug"]
print(planets_list) # Displaying the orginal list.

removed_value = planets_list.pop(2) #remove items that found at 3rd position or 2nd index, also possible only pop() without giving index, which remove the top value which is an end of the value.
print(planets_list) # Displaying a list after the index 2 which Earth is removed the list.
print(f"Human live on {removed_value}") #Output: Human live on Earth.
 
