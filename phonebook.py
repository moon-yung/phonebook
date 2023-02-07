def menu():
    
    print("\n    M A I N  *  M E N U     ")
    print("""
    1.> Display Contacts
    2.> Add Contact
    3.> Delete Contact
    4> Search Contact
    5.> Quit 
                                """)



phoneBook = {}
choice = 0

menu()

while choice !=5:
    choice = int(input("\nEnter number (1-4): >>> "))
    if choice == 1:
        print(" ------------------------")
        print("|    P H O N E B O O K   |")
        print(" ------------------------")
        
        
        if len(phoneBook) == 0:
            print("Phonebook is empty")
        else:
            for x in phoneBook.keys():
                print("Name: ", x, "\tNumber: ", phoneBook[x])


    elif choice == 2:
        print("\nA D D  C O N T A C T")
        name = input("Name: ").lower()
        mobile = int(input("Mobile number: "))
        phoneBook[name] = mobile
        print(phoneBook)

    elif choice ==3:
        print("\nD E L E T E")
        print(phoneBook)
        name = input("Name: ").lower()
        option1 = input("\nAre you sure to delete (Y/N)? >>>  ").upper()
        if option1 == 'Y':
            phoneBook.pop(name)
            print(phoneBook)
            continue
        
        elif option1 == 'N':
            menu()
            continue     
        else:
            print("Enter only Y/N")
            continue  

    elif choice == 4:
        print("\nS E A R C H")
        name = input("Name: ").lower()
        if name in phoneBook:
            print("The number is: ", phoneBook[name])
        else:
            print(name, "Not Found")                  
           
    elif choice !=5:
        menu()