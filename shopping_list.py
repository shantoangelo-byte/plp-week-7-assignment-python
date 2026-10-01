shopping_list = []

while True:
    choice = input("add / remove / show / done: ")


    if choice == "add":
        item = input("What do you want to add? ")
        shopping_list.append(item)
        print("Item added.")



    elif choice == "remove":
        item = input("What do you want to remove? ")

        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed.")
        else:
            print("That item is not on your list.")    

    elif choice == "show":
         for item in shopping_list:
             print(item)

    elif choice == "done":
        print("Goodbye!")
        break         