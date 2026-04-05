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
            phone_number = input("Enter phone").strip()
            email = input("Enter email: ").strip

            contacts = {"name" : name, "phone" : phone_number, "email" : email}

            contacts_list.append(contacts)
            print("Contact added successfully!")

    elif opt == 2:
        search_name = input("Enter a name to search: ").strip().lower()

        found = False

        for each_contact in contacts_list:
            if search_name in each_contact["name"].lower():
                print(f"Contact found!\nName: {each_contact['name']}\nPhone number: {each_contact['phone']}\nEmail: {each_contact['email']}")
                found = True

        if not found:
            print("Contact not found.")

    elif opt == 3:
        print("Update Info.")

        



 