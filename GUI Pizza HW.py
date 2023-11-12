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
    totalmessage = f"Thank you for your order {name}! Your total is ${tc:.2f}."
    messagebox.showinfo("Pizza Order", totalmessage)

root = tk.Tk()
root.title("Pizza Order Calculations")

#charge for pepperoni & sausage but not pineapple, mushroom, or olive
toppings = {
    "Pepperoni: $1.50": 1.50,
    "Sausage: $1.50": 1.50,
    "Bacon: $1.50": 1.50,
    "Pineapple: $0.00": 0.00,
    "Mushroom: $0.00": 0.00,
    "Olive: $0.00": 0.00,
}
#charge based on the amount of dough and detail
crusts = {"Thin Crust: $9.00": 9.00,
          "Thick Crust: $10.00": 10.00,
          "Deep Dish: $11.00": 11.00,
}

name_label = tk.Label(root, text="Name:",fg="yellow", bg="red")
name_label.pack()
name_entry = tk.Entry(root, highlightthickness=1, highlightbackground="black")
name_entry.pack()

topping_label = tk.Label(root, text="Toppings:",fg="yellow", bg="red")
topping_label.pack()

topping_vars = {}
for topping in toppings:
    topping_vars[topping] = tk.IntVar()
    chk = tk.Checkbutton(root, text=topping, variable=topping_vars[topping])
    chk.pack(anchor="w")


crust_label = tk.Label(root, text="Crust:",fg="yellow", bg="red")
crust_label.pack()

crust_vars = {}
for crust in crusts:
    crust_vars[crust] = tk.IntVar()
    radio = tk.Radiobutton(root, text=crust, variable=crust_vars[crust], value=1)
    radio.pack(anchor="w")


calculate_button = tk.Button(root, text="Calculate", command=calc_totalcost,highlightthickness=1, highlightbackground="black")
calculate_button.pack()

root.mainloop()

