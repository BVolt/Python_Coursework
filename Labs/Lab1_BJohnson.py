# Name: Brenden Johnson
# Lab 1 - Task 2 - CS2520.01

print("Welcome to Soda Machine")
print("Alvin's Purchase: ")
eachCan = 5 #5 dollars for each can
bought = 3 #bought 3 cans
print("Alvin need to pay", eachCan * bought, "dollars")
print("Now Terri is using the machine.")
eachCan = int(input("Please enter the unit price: ")) #Fixed type error
bought = int(input("How many can you have you bought?")) # Slight prompt change
print("Terri needs to pay", eachCan * bought, "dollars")

#Output
#Welcome to Soda Machine
#Alvin's Purchase:
#Alvin need to pay 15 dollars
#Now Terri is using the machine.
#Please enter the unit price: 6
#How many can you have you bought?4
#Terri needs to pay 24 dollars

#Process finished with exit code 0