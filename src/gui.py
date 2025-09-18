import tkinter as tk
from tkinter import ttk, messagebox
from converters import LengthConverter, MassConverter, TemperatureConverter
from history import add_record, load_history, clear_history


class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("500x450")

        self.category = tk.StringVar(value="Length")
        self.value = tk.StringVar()
        self.from_unit = tk.StringVar()
        self.to_unit = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()
        self.update_units()
        self.load_history()


    def create_widgets(self):
        ttk.Label(self.root, text="Category").pack()
        categories = ["Length", "Mass", "Temperature"]
        category_menu = ttk.Combobox(
            self.root, textvariable=self.category, values=categories
        )
        category_menu.bind("<<ComboboxSelected>>", lambda e: self.update_units())
        category_menu.pack()

        ttk.Label(self.root, text="Value").pack()
        ttk.Entry(self.root, textvariable=self.value).pack()

        ttk.Label(self.root, text="From").pack()
        self.from_menu = ttk.Combobox(self.root, textvariable=self.from_unit)
        self.from_menu.pack()

        ttk.Label(self.root, text="To").pack()
        self.to_menu = ttk.Combobox(self.root, textvariable=self.to_unit)
        self.to_menu.pack()

        ttk.Button(self.root, text="Convert", command=self.convert).pack(pady=10)

        ttk.Label(self.root, text="Result").pack()
        ttk.Label(self.root, textvariable=self.result).pack()

        ttk.Label(self.root, text="History").pack()
        self.history_listbox = tk.Listbox(self.root, height=10)
        self.history_listbox.pack(fill="both", expand=True)

        ttk.Button(self.root, text="Clear History", command=self.clear_history).pack(
            pady=5
)

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
