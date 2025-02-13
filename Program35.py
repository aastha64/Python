import tkinter as tk
import os

def save_item_details():
    item_code = entry_code.get()
    item_name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    
    file_path = r"C:\Users\sarth\Desktop\Training\ITEM_DETAIL.csv"
    
    with open(file_path, "a") as file:
        file.write(f"{item_code}, {item_name}, {quantity}, {price}\n")
    
    entry_code.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

root = tk.Tk()
root.title("Item_Detail")
root.geometry("300x250")

tk.Label(root, text = "Item_Code:").grid(row = 0, column = 0, padx = 10, pady = 5)
entry_code = tk.Entry(root)
entry_code.grid(row = 0, column = 1, padx = 10, pady = 5)

tk.Label(root, text = "Item_Name:").grid(row = 1, column = 0, padx = 10, pady = 5)
entry_name = tk.Entry(root)
entry_name.grid(row = 1, column = 1, padx = 10, pady = 5)

tk.Label(root, text = "Quantity:").grid(row = 2, column = 0, padx = 10, pady = 5)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row = 2, column = 1, padx = 10, pady = 5)

tk.Label(root, text="Price:").grid(row = 3, column = 0, padx = 10, pady = 5)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add", command=save_item_details).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()