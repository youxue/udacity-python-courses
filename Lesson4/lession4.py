# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:03:06 2020

@author: WEN
"""

#Udacity Python Course - Lession 4 Control Flow
#Part 3 if
#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10 
    
print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number
number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 75

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age or age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
    
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)
print("\n")


#Part 4 quiz 1
points = 130  # use this input to make your submission
result = False
# write your if statement here
if points >= 1 and points <= 50:
    prize_name = "wooden rabbit"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    prize_name = "wafer-thin mint"
elif points <= 200:
    prize_name = "penguin"
else:
    result = "Error! No such scores."

if not result:
    result = "Congratulations! You won a {}!".format(prize_name)

print(result)
print("\n")


#Part 9 for loop
#Part 10 quiz 1
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
i = 0
for name in names:
    
    name = name.lower().replace(" ", "_")
    usernames.append(name)
    names[i]=name
    i += 1

print(usernames) 
print(names)
print("\n")  


#Part 10 quiz 2
#range(start, stop, step) generate a sequence start from the start, ended at stop - 1, with step the step
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ","_")
print(usernames)
print("\n") 


#Part 10 quiz 3
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    #token.find()

    if(token[0] == "<" and token[-1] == ">"):      
        count += 1

print(count)
print("\n") 


#Part 10 quiz 4
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>" + item + "</li>" + "\n"
    #html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"
print(html_str)
print("\n") 


#Part 13 While, quiz 1
limit = 40
nearest_square = 1
while((nearest_square + 1)**2 < limit):
    nearest_square += 1
nearest_square *= nearest_square

print(nearest_square)
print("\n") 


#Part 15 break & continue
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))
print("\n")



#Part 16 quiz 1 Go throw headlines and create a 140 length str. need a " " between titles
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
length_limit = 140
news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker +=  " " + headline
    if len(news_ticker) < length_limit + 1:

        continue
    else:
        news_ticker = news_ticker[1 : length_limit + 2]
        break

'''for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break '''

print(news_ticker)