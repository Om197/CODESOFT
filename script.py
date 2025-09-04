# Write each code to separate python files for user download

todo_code = '''
def todo_app():
    todo_list = []
    while True:
        print("1. Add task\n2. View tasks\n3. Update task\n4. Delete task\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            task = input("Enter new task: ")
            todo_list.append(task)
            print("Task added.")
        elif choice == '2':
            for i, t in enumerate(todo_list):
                print(f"{i+1}. {t}")
        elif choice == '3':
            idx = int(input("Task number to update: ")) - 1
            if 0 <= idx < len(todo_list):
                new_task = input("Enter new task: ")
                todo_list[idx] = new_task
                print("Task updated.")
        elif choice == '4':
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(todo_list):
                todo_list.pop(idx)
                print("Task deleted.")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
    print("Exiting To-Do List App.")

todo_app()
'''

calc_code = '''
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Operations: +, -, *, /")
    op = input("Choose operation: ")
    result = None
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b != 0:
            result = a / b
        else:
            result = "Division by zero error"
    else:
        result = "Invalid operation"
    print(f"Result: {result}")

calculator()
'''

pwgen_code = '''
import random
import string
def password_generator():
    length = int(input("Enter desired password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

password_generator()
'''

rps_code = '''
import random
def rock_paper_scissors():
    score_user = 0
    score_comp = 0
    choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        if user == comp:
            print("It's a tie.")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'scissors' and comp == 'paper') or \
             (user == 'paper' and comp == 'rock'):
            print("You win!")
            score_user += 1
        elif user in choices:
            print("Computer wins!")
            score_comp += 1
        else:
            print("Invalid choice.")
        print(f"Score: User={score_user}, Computer={score_comp}")
        again = input("Play again? (y/n): ")
        if again != 'y':
            break

rock_paper_scissors()
'''

contact_code = '''
def contact_book():
    contacts = []
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            print("Contact added.")
        elif choice == '2':
            for i, c in enumerate(contacts):
                print(f"{i+1}. {c['name']} - {c['phone']}")
        elif choice == '3':
            search = input("Search by name or phone: ").lower()
            found = [c for c in contacts if search in c['name'].lower() or search in c['phone']]
            for c in found:
                print(c)
        elif choice == '4':
            idx = int(input("Contact number to update: ")) - 1
            if 0 <= idx < len(contacts):
                print("Updating contact...")
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                contacts[idx] = {'name': name, 'phone': phone, 'email': email, 'address': address}
                print("Contact updated.")
        elif choice == '5':
            idx = int(input("Contact number to delete: ")) - 1
            if 0 <= idx < len(contacts):
                contacts.pop(idx)
                print("Contact deleted.")
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
    print("Exiting Contact Book.")

contact_book()
'''

with open('todo.py', 'w') as f:
    f.write(todo_code)
with open('calculator.py', 'w') as f:
    f.write(calc_code)
with open('password_generator.py', 'w') as f:
    f.write(pwgen_code)
with open('rps_game.py', 'w') as f:
    f.write(rps_code)
with open('contact_book.py', 'w') as f:
    f.write(contact_code)

print("All project files saved: todo.py, calculator.py, password_generator.py, rps_game.py, contact_book.py")
