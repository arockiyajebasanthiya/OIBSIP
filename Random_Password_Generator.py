#import modules
import tkinter as tk
from tkinter import messagebox
import random as rd
import pyperclip as pk
import string

def random_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    try:
        char_count=int(entry_num1.get())
        integer_count=int(entry_num2.get())
        symbol_count=int(entry_num3.get())
        password_list=[]
        for i in range(1,char_count+1):
            password_list.append(rd.choice(letters))
        for i in range(1,integer_count+1):
            password_list.append(rd.choice(numbers))
        for i in range(1,symbol_count+1):
            password_list.append(rd.choice(symbols))
        rd.shuffle(password_list)
        password = ""
        for char in password_list:
            password += char

        result_var.set(password)
        pk.copy(password)
        instruction4_label=tk.Label(root,text="Password copied Successfully")
        instruction4_label.pack(side=tk.LEFT,padx=10,pady=10)

#ValueError Exception
    except ValueError:
        messagebox.showinfo("Alert","Please enter a Valid integer")
   
                         
root=tk.Tk()
root.title("Random password Generator")
instruction1_label=tk.Label(root,text="How many characters do you desire?")
instruction1_label.pack(pady=10)
entry_num1=tk.Entry(root,width=10)
entry_num1.pack(pady=5)

instruction2_label=tk.Label(root,text="How many integers are you aiming for?")
instruction2_label.pack(pady=10)

entry_num2=tk.Entry(root,width=10)
entry_num2.pack(pady=5)

instruction3_label=tk.Label(root,text="How many special characters do you want?")
instruction3_label.pack(pady=10)

entry_num3=tk.Entry(root,width=10)
entry_num3.pack(pady=5)

calculate_button=tk.Button(root,text="Submit",command=random_password)
calculate_button.pack(pady=20)

result_var=tk.StringVar()
result_label=tk.Label(root,textvariable=result_var,width=10)
result_label.pack(pady=10)

root.mainloop()


                     
    

