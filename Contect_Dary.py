import tkinter as tk
from tkinter import messagebox


def add_contect():
    name = name_enty.get()
    phone = phone_number_entry.get()
    
    if name != "" and phone != "":
        contect_list.insert(tk.END, f"{name} : {phone}")
        name_enty.delete(0, tk.END)
        phone_number_entry.delete(0, tk.END)
        
    else:
        messagebox.showerror("Value Error")
        
def edit_contect():
    try:
        select = contect_list.curselection()[0]
        select_text = contect_list.get(select)
    
        name , phone = select_text.split(" : ")
        name_enty.delete(0, tk.END)
        phone_number_entry.delete(0, tk.END)
    
        name_enty.insert(0, name)
        phone_number_entry.insert(0, phone)
    
        contect_list.delete(select)
    except:
        messagebox.showerror('Please Select')

def delete_contect():
    try:
        select = contect_list.curselection()[0]
        contect_list.delete(select)
        messagebox.showinfo('deleted')
    except:
        messagebox.showerror("Please Slect")
        
root = tk.Tk()
root.title('Contact Diary')
root.geometry('400x600')


title = tk.Label(root, text='CONTACT DIARY', font=('arial', 12, 'bold'))
title.pack(pady=5)

name = tk.Label(root, text='Name :- ', font=('arial', 12))
name.pack(pady=5)
name_enty = tk.Entry(root, font=('arial', 10))
name_enty.pack(pady=5)

phone_number = tk.Label(root, text="Phone Number :- ", font=('arial', 12))
phone_number.pack(pady=5)
phone_number_entry = tk.Entry(root, font=('arial', 10))
phone_number_entry.pack(pady=5)

save_btn = tk.Button(root, text='Add', bg='green', command=add_contect)
save_btn.pack(pady=5)

edit_btn = tk.Button(root, text="Edit", bg='yellow', command=edit_contect)
edit_btn.pack(pady=2)

delete_btn = tk.Button(root, text='Delete', bg='red', command=delete_contect)
delete_btn.pack(pady=5)


contect_list = tk.Listbox(root, font=('arial', 12, 'bold'))
contect_list.pack(pady=10)





root.mainloop()