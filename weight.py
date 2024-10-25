import tkinter as tk
from tkinter import ttk, messagebox

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def kg_to_grams(kg):
    return kg * 1000

def grams_to_kg(grams):
    return grams / 1000

def pounds_to_grams(pounds):
    return pounds * 453.592

def grams_to_pounds(grams):
    return grams / 453.592

def convert_weight():
    try:
        weight = float(entry_weight.get())
        conversion_type = combo_conversion.get()

        if conversion_type == 'Kilograms to Pounds':
            result = kg_to_pounds(weight)
            label_result.config(text=f"{weight} kg = {result:.2f} lbs")
        elif conversion_type == 'Pounds to Kilograms':
            result = pounds_to_kg(weight)
            label_result.config(text=f"{weight} lbs = {result:.2f} kg")
        elif conversion_type == 'Kilograms to Grams':
            result = kg_to_grams(weight)
            label_result.config(text=f"{weight} kg = {result:.2f} grams")
        elif conversion_type == 'Grams to Kilograms':
            result = grams_to_kg(weight)
            label_result.config(text=f"{weight} grams = {result:.2f} kg")
        elif conversion_type == 'Pounds to Grams':
            result = pounds_to_grams(weight)
            label_result.config(text=f"{weight} lbs = {result:.2f} grams")
        elif conversion_type == 'Grams to Pounds':
            result = grams_to_pounds(weight)
            label_result.config(text=f"{weight} grams = {result:.2f} lbs")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

def clear_fields():
    entry_weight.delete(0, tk.END)
    label_result.config(text="")
    combo_conversion.set("Kilograms to Pounds")  # Reset to default

# Create the main window
root = tk.Tk()
root.title("Weight Converter")

# Create input label and entry
label_weight = tk.Label(root, text="Enter weight:")
label_weight.pack(pady=10)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Create conversion options
label_conversion = tk.Label(root, text="Select conversion type:")
label_conversion.pack(pady=10)
combo_conversion = ttk.Combobox(root, values=[
    "Kilograms to Pounds", 
    "Pounds to Kilograms",
    "Kilograms to Grams",
    "Grams to Kilograms",
    "Pounds to Grams",
    "Grams to Pounds"
])
combo_conversion.set("Kilograms to Pounds")  # Set default selection
combo_conversion.pack(pady=5)

# Create convert button
button_convert = tk.Button(root, text="Convert", command=convert_weight)
button_convert.pack(pady=20)

# Create clear button
button_clear = tk.Button(root, text="Clear", command=clear_fields)
button_clear.pack(pady=5)

# Create label for result
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Start the GUI event loop
root.mainloop()
