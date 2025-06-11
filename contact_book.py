import mysql.connector

conn=mysql.connector.connect(
    user='root',
    host='localhost',
    password='12345',
    database='contact_book'
)

mycur=conn.cursor()

def display_contacts():
    mycur.execute("select * from contact_logs")
    contacts=mycur.fetchall()
    if not contacts:
        print("No Contacts Found")
    else:
        print(f"{'Name':<15} {'Phone no':<20} {'Email':<30} {'Address':<20}")
        print("-"*100)
        for i in contacts:
            name,phone,email,address=i
            print(f"{name:<15} {phone:<20} {email:<30} {address:<20}")
        
        
def add_contacts():
    while True:
        name=input("Enter name : ")
        phone=input("Enter phone number : ")
        email=input("Enter email : ")
        address=input("Enter address : ")
        mycur.execute("insert into contact_logs (name,phone,email,address) values (%s,%s,%s,%s)",(name,phone,email,address))
        conn.commit()
        print("\nContact added successfully\n")
        ans=input("Add more (Y/N) : ").lower().strip()
        print()
        if ans=='n':
            break

def search_contact():
    search_elem=input("Enter search element : ")
    print()
    mycur.execute("select * from contact_logs where name like %s or phone like %s",(f"%{search_elem}%",f"%{search_elem}%"))
    contact=mycur.fetchall()
    if not contact:
        print("No contact found")
    else:
        print(f"{'Name':<15} {'Phone':<20} {'Email':<30} {'Address':<20}")
        print("-"*100)
        for i in contact:
            name,phone,email,address=i
            print(f"{name:<15} {phone:<20} {email:<30} {address:<20}")
    
    
def update_contact():
    name=input("Enter name : ")
    mycur.execute("select * from contact_logs where name like %s",(f"%{name}%",))
    contact=mycur.fetchall()
    if not contact:
        print("Contact Not Found")
        return
    print(f"{'Name':<15} {'Phone':<20} {'Email':<30} {'Address':<20}")
    print("-"*95)
    for i in contact:
        name,phone,email,address=i
        print(f"{name:<15} {phone:<20} {email:<30} {address:<20}")
    print()
    while True:
        update=input("What do you want to update (Name/Phone/Email/Address) : ").lower().strip()
        if update=='name':
            new_name=input("Enter new name : ")
            mycur.execute("update contact_logs set name=%s where name=%s",(new_name,name))
            conn.commit()
        elif update=='phone':
            new_phone=input("Enter new phone number : ")
            mycur.execute("update contact_logs set phone=%s where name=%s",(new_phone,name))
            conn.commit()
        elif update=='email':
            new_email=input("Enter new email : ")
            mycur.execute("update contact_logs set email=%s where name=%s",(new_email,name))
            conn.commit()
        elif update=='address':
            new_address=input("Enter new address : ")
            mycur.execute("update contact_logs set address=%s where name=%s",(new_address,name))
            conn.commit()
        print("\nUpdated successfully\n")
        ans=input("Update anything else (Y/N) : ").lower().strip()
        if ans=='n':
            break
                               
            
def delete_contact():
    name=input("Enter name : ")
    mycur.execute("select * from contact_logs where name like %s",(f"%{name}%",))
    contact=mycur.fetchall()
    if not contact:
        print("No contact found")
        return
    print("Matched Content : ")
    print(f"{'Name':<15} {'Phone':<20} {'Email':<30} {'Address':<20}")
    print("-"*100)
    for i in contact:
        name,phone,email,address=i
        print(f"{name:<15} {phone:<20} {email:<30} {address:<20}")
    print()
    confirm=input("Are you sure you want to delete this contact (Y/N) : ").lower().strip()
    if confirm=='y':
        mycur.execute("delete from contact_logs where name like %s",(f"%{name}%",))
        print("\nContact deleted successfully")
    else:
        print("\nDeletion cancelled")
    conn.commit()
    

    
def main():
    while True:
        print("\n------ Contact Book ------\n")
        print("1. Display contacts")
        print("2. Add new contact")
        print("3. Search a contact")
        print("4. Update contact")
        print("5. Delete a contact")
        print("6. Exit\n")
        try:
            choice=int(input("Choose an option : "))
        except ValueError:
            print("Enter a valid option")
            continue
        print()
        if choice==1:
            display_contacts()
            print()
        elif choice==2:
            add_contacts()
            print()
        elif choice==3:
            search_contact()
            print()
        elif choice==4:
            update_contact()
            print()
        elif choice==5:
            delete_contact()
            print()
        elif choice==6:
            break
        else:
            print("Invalid option")

    
    
main()