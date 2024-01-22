#Sebastian de Wijkerslooth
#1/18/23
#To-Do List #2


#Functions


glist = ["apple", "banana", "cherry"]
#This function will allow me to continuously rerun the code until I choose for it to quit
def replay():
    displaymenu()
print("Welcome to your Grocery List! Your current list has, " + str(glist))
#This funtion holds the code for the whole grocery list
def displaymenu():
    x = input("Would you like to \n 1) Add a task to the to-do list \n 2) View the current to-do list \n 3) Mark a current task completed \n 4) Remove a task from the to-do list \n 5) Remove all tasks from the to-do list \n 6) Sort the list alphabetically \n 7) Print the number of items on the to-do list \n 8) Exit the program \n (1)(2)(3)(4)(5)(6)(7)(8)")
    if x == "1":
        addglist = input("What would you like to add to you grocery list? ")
        glist.append(addglist)
        print("Your list now has " + str(glist))
        displaymenu()
    if x == "2":
        print("Your current list is " + str(glist))
        displaymenu()
    if x == "3":
        print ("What item on your grocery list would you like to mark as completed?")
        comp = input("Type in the item ")
        y = glist.index(comp)
        glist[y] = comp + "[X]"
        print(glist)
        displaymenu()
    if x == "4":
        print("Which item would you like to remove?")
        remove = input("Select which item to remove : ")
        y = glist.index(remove)
        glist.pop(y)
        replay()
    if x == "5":
        glist.clear()
    if x == "6":
        glist.sort()
        print("Your current list is " + str(glist))
    if x == "7":
        print("The Number of Items in the List is: " + str(len(glist)))
    if x == "8":
        quit()
    replay()
   
#Main
displaymenu()