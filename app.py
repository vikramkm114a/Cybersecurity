import tkinter as tk
from tkinter import messagebox


def add():
    username = entryName.get() #accepting user input
    password = entryPassword.get() #accepting password input from the user
    if username and password: #if username and password are entered
        with open("passwords.txt", 'a') as f: 
            f.write(f"{username} {password}\n") #open file: passwords.txt and add credentials to file
        messagebox.showinfo("Success", "Password added!") #display success message using Tkinter messagebox
    else:
        messagebox.showerror("Error", "Please fill out both fields") #display error message using Tkinter messagebox
        
def get():
    username = entryName.get() #accepting user input
   
    passwords = {} #creating empty dictionary to store data
    try:
        with open("passwords.txt", 'r') as f: #open and read passwords.txt
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1] #creating key-value pair of username and password
    except:
        print("Error!") #displaying error message
        
    if passwords: #if username exists, display corresponding password
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        else: #otherwise show error message
            mess += "No such username exists!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "Empty List!")
        
def getlist():
    passwords = {} #create a dictionary to add username : password pairs
    try: #add try block to catch errors such as empty files
        with open("passwords.txt", 'r') as f: #open and read passwords.txt
            for k in f: 
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("No passwords found!")
        
    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            mess += f"Password for {name} is {password}\n" #generating a proper message
        messagebox.showinfo("Passwords", mess) #showing the message
    else: #if file is empty, display error message
        messagebox.showinfo("Passwords", "Empty List!")
        
def delete():
    username = entryName.get()
    temp_passwords = []
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")
        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(line)
        
        messagebox.showinfo("Success", f"User {username} deleted successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x270")
    app.title("Password Manager")

    # Username block
    labelName = tk.Label(app, text="USERNAME:")
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = tk.Entry(app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    # Password block
    labelPassword = tk.Label(app, text="PASSWORD:")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = tk.Entry(app)
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    # Add button
    buttonAdd = tk.Button(app, text="Add", command=add)
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

    # Get button
    buttonGet = tk.Button(app, text="Get", command=get)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    # List Button
    buttonList = tk.Button(app, text="List", command=getlist)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tk.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    app.mainloop()