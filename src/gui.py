import tkinter as tk
from tkinter import ttk, messagebox
from converters import LengthConverter, MassConverter, TemperatureConverter
from history import add_record, load_history, clear_history

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("500x500")

        # Variables
        self.category = tk.StringVar(value="Length")
        self.value = tk.StringVar()
        self.from_unit = tk.StringVar()
        self.to_unit = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()
        self.update_units()
        self.load_history()

    def clear_history(self):
        """Clear the history from file and listbox."""
        clear_history()
        self.history_listbox.delete(0, tk.END)

    def create_widgets(self):
        # Category
        ttk.Label(self.root, text="Category").pack()
        categories = ["Length", "Mass", "Temperature"]
        category_menu = ttk.Combobox(self.root, textvariable=self.category, values=categories)
        category_menu.bind("<<ComboboxSelected>>", lambda e: self.update_units())
        category_menu.pack()

        # Value
        ttk.Label(self.root, text="Value").pack()
        ttk.Entry(self.root, textvariable=self.value).pack()

        # From unit
        ttk.Label(self.root, text="From").pack()
        self.from_menu = ttk.Combobox(self.root, textvariable=self.from_unit)
        self.from_menu.pack()

        # To unit
        ttk.Label(self.root, text="To").pack()
        self.to_menu = ttk.Combobox(self.root, textvariable=self.to_unit)
        self.to_menu.pack()

        # Button
        ttk.Button(self.root, text="Convert", command=self.convert).pack(pady=10)

        # Result
        ttk.Label(self.root, text="Result").pack()
        ttk.Label(self.root, textvariable=self.result).pack()

        # History
        ttk.Label(self.root, text="History").pack()
        self.history_listbox = tk.Listbox(self.root, height=10)
        self.history_listbox.pack(fill="both", expand=True)

        # Clear History button
        ttk.Button(self.root, text="Clear History", command=self.clear_history).pack(pady=10)

    def update_units(self):
        cat = self.category.get()
        if cat == "Length":
            units = list(LengthConverter.units.keys())
        elif cat == "Mass":
            units = list(MassConverter.units.keys())
        else:
            units = ["C", "F", "K"]

        self.from_menu["values"] = units
        self.to_menu["values"] = units
        if units:
            self.from_unit.set(units[0])
            self.to_unit.set(units[1] if len(units) > 1 else units[0])

    def convert(self):
        try:
            value = float(self.value.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a number")
            return

        cat = self.category.get()
        if cat == "Length":
            converter = LengthConverter()
        elif cat == "Mass":
            converter = MassConverter()
        else:
            converter = TemperatureConverter()

        result = converter.convert(value, self.from_unit.get(), self.to_unit.get())
        self.result.set(str(result))

        add_record(value, self.from_unit.get(), self.to_unit.get(), result, cat)
        self.load_history()

    def load_history(self):
        self.history_listbox.delete(0, tk.END)
        for record in load_history():
            line = f"{record['value']} {record['from']} -> {record['result']} {record['to']} ({record['category']})"
            self.history_listbox.insert(tk.END, line)

def main():
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
