# TRY IT YOURSELF

#exerise 3.1 Names
'''Store the names of a few of your friends in alist called names.
Print each person's by accessing each element in the ist, one at a time.'''
names = ["Alex", "Micheal", "James", "Abel"] #Defining and assigning list.
print(names[0]) #Output Alex
print(names[1]) #Output Micheal
print(names[2]) #Output James
print(names[3]) #Output Abel

# exericse 3.2 Greating 
'''Start with the list you used in Exercise 3.1, but instead of just printing each person's name, print a message to them.
The text of each message should be the samae , but each message should be personalized with the person's name'''
print(f"Hi {names[0]}, How was your day!")
print(f"Hi {names[1]}, How was your day?")
print(f"Hi {names[2]}, How was your day?")
print(f"Hi {names[3]}, How was the your day")

# exercise 3.3 Your Own List
'''Think of your favorite mdoe of transportation, such as a motorcycle or a car, and make a list that stores several examples/
Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle.'''
cars = ["Tesla", "BYD", "Toyota", "Lamborghini", "Ferarri"]
message = ["I would like to own a ", "I would like to own an "]
print(message[0] + cars[0])

# exercise 3.4 Guest list
'''If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.'''
import datetime
invite_names = ["Donald Trump", "Vladimir Putin", "Xi Jinping", "Benjamin Netanyahu", "Abiy Ahmed"]
date = datetime.datetime.now()
date_str = str(date)
invitation_message =f"I'm inviting to \nmy Birthday Party which is Jun 29 2025\nI am sure as I will meet you that day."
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[0]} {invitation_message}")
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[1]} {invitation_message}")
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[2]} {invitation_message}")

# exercise 3.5 changing Guest list
import datetime
invite_names = ["Donald Trump", "Vladimir Putin", "Xi Jinping", "Benjamin Netanyahu", "Abiy Ahmed"]
date = datetime.datetime.now()
date_str = str(date)
invitation_message =f"I'm inviting to \nmy Birthday Party which is Jun 29 2025\nI am sure as I will meet you that day."

'''You just heard that one of your guests can't make the dinner, so you need to send out a new set of inviations .
You'll have to think of someone else to invite'''
print(f"the name of guest who can't came to party.\n {invite_names[1]}\n {invite_names[0]} \n")
del invite_names[0]
del invite_names[1]
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[0]} {invitation_message}")
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[1]} {invitation_message}")
print(f"{date_str.rjust(50)} \nHello Mr {invite_names[2]} {invitation_message}")

# exercise 3.6 More Guests
'''You just found a bigger dinner table, so now more space is available. Think of three most guests to inbite to dinner.
- Start with your program from Exercise 3.4 or Exercise 3.5. Add a print() call to the end of your program informing people 
that you found a bigger dinner table.
- Use insert() to add new guest to the beginning of your list.
- Use insert() to add one new guest to the middle of your list.
- Use append() to add one new guest to the end of your list.
- Print a new set of inviatation messages, one for each person in your list.'''
import datetime
invite_names = ["Donald Trump", "Vladimir Putin", "Xi Jinping", "Benjamin Netanyahu", "Abiy Ahmed"]
date = datetime.datetime.now()
date_str = str(date)
invitation_message =f"I'm inviting to \nmy Birthday Party which is Jun 29 2025\nI am sure as I will meet you that day."
print("Name of a list who they added now \n - Benjamin Natanyahu \n - Robert Mugabe - \n Cristino Ronlado")
invite_names.insert(0, "Benjamin Natanyahu")
mid = (len(invite_names) - 1) / 2
invite_names.insert(int(mid), "Robert Mugabe")
invite_names.append("Cristino Ronaldo")
for i in range(len(invite_names)):
    print(f"{date_str.rjust(50)} \nHello Mr {invite_names[i]} {invitation_message}")

# exercise 3.7 Shrinking Guest list
''' You just found out that your new dinner won't arrive in time for the dinner,
and you have space for only two guests.
- Start with your program from Exercise 3.6. Add a new line that prints a message
saying that you can invite only two people for dinner.
- Use pop() to remove guests from your list one at a time only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
- Print a message to each of the people still on your list, letting them know they're still invited.
- Use delto remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.'''


print("Name of a list who they added now \n - Benjamin Natanyahu \n - Robert Mugabe - \n Cristino Ronlado")
invite_names.insert(0, "Benjamin Natanyahu")
mid = (len(invite_names) - 1) / 2
invite_names.insert(int(mid), "Robert Mugabe")
invite_names.append("Cristino Ronaldo")
for i in range(len(invite_names)):
    print(f"{date_str.rjust(50)} \nHello Mr {invite_names[i]} {invitation_message}")


print("you can invite only two people for dinner.") # message written after checked there only two table are arrived for dinner.

for i in range(len(invite_names)): #len(invite(names)) is 6 but when using range it count from 0 so its from 0 abto 5.
    if(i >= 2):
        break
    else:
        print(f"Hello {invite_names.pop()}, We are you sorry you can't invite to the dinner.")
while(len(invite_names) >= 0):
    print(f"Mr {invite_names[0]}, Do forget to came you are still invited.")
    del invite_names[0] # remove a person after writing remember card.
print(invite_names) #empty name list.