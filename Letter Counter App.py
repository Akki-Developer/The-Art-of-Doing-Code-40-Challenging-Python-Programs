print("Welcome to the Letter Counter App")
name = input("\nWhat is your name: ")
print("Hello "+name+"!")
print("\nI will count the number of times that a specific letter occurs in a message.")
message= input("\nPlease enter a message: ")
letter=input("\nWhich letter would you like to count the occurences of: ")
message=message.lower()
letter=letter.lower()
count_res=message.count(letter)
print(name+", your message has "+str(count_res)+" "+letter+"'s in it.")