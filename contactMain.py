contacts = {

}

contacts_list = [

]

while True:
    print("""1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit""")
    
    opt = int(input("Enter the number: "))

    if opt == 1:
        name = input("Enter name: ").strip()
        
        if not name:
            print("Name cannot be empty!")

        else:
            phone_number = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()

            contacts = {"name" : name, "phone" : phone_number, "email" : email}

            contacts_list.append(contacts)
            print("Contact added successfully!")

    elif opt == 2:
        print("All contacts")
        for each_contact in contacts_list:
                print(f"Name: {each_contact['name']}\nPhone number: {each_contact['phone']}\nEmail: {each_contact['email']}")


    elif opt == 3:
        search_name = input("Enter a name to search: ").strip().lower()

        found = False

        for each_contact in contacts_list:
            if search_name in each_contact["name"].lower():
                print(
                    f"Contact found!\nName: {each_contact['name']}\nPhone number: {each_contact['phone']}\nEmail: {each_contact['email']}")
                found = True

        if not found:
            print("Contact not found.")

        elif opt == 4:
            print("Update Contact")

            search_name = input("Enter a name to update: ").strip().lower()

            found = False
            for each_contact in contacts_list:
                if search_name in each_contact["name"].lower():
                    each_contact["name"] = search_name
                    found = True

                    new_name = input("Enter new name (leave blank to keep current): ").strip()
                    new_phone = input("Enter new phone (leave blank to keep current): ").strip()
                    new_email = input("Enter new email (leave blank to keep current): ").strip()

                    if new_name :
                        new_name["phone"] = new_phone
                    if new_phone :
                        each_contact["phone"] = new_phone
                    if new_email :
                        each_contact["email"] = new_email
                    print("Contact updated successfully!")
                    found = True
                    break

                if not found:
                    print("Contact not found.")

        elif opt == 5:
            print("Delete Contact")

            name_delete = input("Enter a name to delete: ").strip().lower()
            found = False

            for index, contacts in enumerate (contacts_list):
                if name_delete == contacts["name"].lower():
                    contacts_list.pop(index)
                    print("Contact deleted.")
                    found = True
                    break
            
        if not found:
            print("Contact not found.")

        elif opt == 6:
            print("You exited the program")
            break

        else:   
            print("Invalid option number.")


        



 