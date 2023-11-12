import tkinter as tk
from tkinter import messagebox

def calc_totalcost():
    tc = 0

    for topping, cost in toppings.items():
        if topping_vars[topping].get():
            tc += cost

    for crust, cost in crusts.items():
        if crust_vars[crust].get():
            tc += cost

    name = name_entry.get()
    totalmessage = f"Thank you for your order, {name}! Your total is ${tc:.2f}."
    messagebox.showinfo("Pizza Order", totalmessage)

root = tk.Tk()
root.title("Pizza Order Calculations")

toppings = {
    "pepperoni": 1.50,
    "sausage": 1.50,
    "bacon": 1.50,
    "pineapple": 1.00,
    "mushroom": 1.00,
    "olive": 1.00,
}

crusts = {"Thin Crust": 2.00,
          "Thick Crust": 3.00,
          "Deep Dish": 4.00,
}

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

topping_label = tk.Label(root, text="Toppings:")
topping_label.pack()

topping_vars = {}
for topping in toppings:
    topping_vars[topping] = tk.IntVar()
    chk = tk.Checkbutton(root, text=topping, variable=topping_vars[topping])
    chk.pack(anchor="w")

# Create labels and radio buttons for crust
crust_label = tk.Label(root, text="Crust:")
crust_label.pack()

crust_vars = {}
for crust in crusts:
    crust_vars[crust] = tk.IntVar()
    radio = tk.Radiobutton(root, text=crust, variable=crust_vars[crust], value=1)
    radio.pack(anchor="w")

# Create Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calc_totalcost)
calculate_button.pack()

root.mainloop()

