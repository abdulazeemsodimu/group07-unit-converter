import tkinter as tk
from tkinter import ttk, messagebox
from src.converters import LengthConverter, MassConverter, TemperatureConverter
from src.history import add_record, load_history, clear_history

class UnitConverterApp:
    """
    A Tkinter-based Unit Converter GUI application.

    Features:
        - Convert values between Length, Mass, and Temperature units.
        - Maintain a conversion history (stored in JSON file).
        - Display conversion history in a listbox.
        - Clear conversion history when needed.
    """
    def __init__(self, root):
         """
        Initialize the Unit Converter app.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
         
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("500x500")

        # Tkinter variables for UI data binding
        self.category = tk.StringVar(value="Length")
        self.value = tk.StringVar()
        self.from_unit = tk.StringVar()
        self.to_unit = tk.StringVar()
        self.result = tk.StringVar()

        # Build UI and initialize state
        self.create_widgets()
        self.update_units()
        self.load_history()

    def clear_history(self):
        """
        Clear the conversion history from file and remove items from the listbox.
        """
        clear_history()
        self.history_listbox.delete(0, tk.END)

    def create_widgets(self):
        """
        Create and layout all the widgets in the application window.
        Includes:
            - Category dropdown
            - Input value entry
            - From/To unit dropdowns
            - Convert button
            - Result display
            - History display
            - Clear history button
        """
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

        # Convert button
        ttk.Button(self.root, text="Convert", command=self.convert).pack(pady=10)

        # Result display
        ttk.Label(self.root, text="Result").pack()
        ttk.Label(self.root, textvariable=self.result).pack()

        # History label and listbox
        ttk.Label(self.root, text="History").pack()
        self.history_listbox = tk.Listbox(self.root, height=10)
        self.history_listbox.pack(fill="both", expand=True)

        # Clear History button
        ttk.Button(self.root, text="Clear History", command=self.clear_history).pack(pady=10)

    def update_units(self):
        """
        Update available units in the dropdown menus based on the selected category.
        Supported categories:
            - Length: m, km, cm, mm
            - Mass: g, kg, mg
            - Temperature: C, F, K
        """
        cat = self.category.get()
        if cat == "Length":
            units = list(LengthConverter.units.keys())
        elif cat == "Mass":
            units = list(MassConverter.units.keys())
        else:
            units = ["C", "F", "K"]

        # Update dropdown menus
        self.from_menu["values"] = units
        self.to_menu["values"] = units

        # Set defaults (first two available units)
        if units:
            self.from_unit.set(units[0])
            self.to_unit.set(units[1] if len(units) > 1 else units[0])

    def convert(self):
        """
        Perform unit conversion based on the current input and category.
        - Validates input value.
        - Uses the appropriate converter class (Length, Mass, Temperature).
        - Updates the result label and saves the record to history.
        """
        # Validate numeric input
        try:
            value = float(self.value.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a number")
            return

        # Choose the right converter class
        cat = self.category.get()
        if cat == "Length":
            converter = LengthConverter()
        elif cat == "Mass":
            converter = MassConverter()
        else:
            converter = TemperatureConverter()

        # Perform conversion
        result = converter.convert(value, self.from_unit.get(), self.to_unit.get())
        self.result.set(str(result))

        # Save record to history file
        add_record(value, self.from_unit.get(), self.to_unit.get(), result, cat)

        # Refresh history listbox
        self.load_history()

    def load_history(self):
        """
        Load and display conversion history in the listbox.
        Shows most recent conversions at the top.
        """
        # Clear listbox
        self.history_listbox.delete(0, tk.END)
        
        # Format each history record for display
        for record in load_history():
            line = f"{record['value']} {record['from']} -> {record['result']} {record['to']} ({record['category']})"
            self.history_listbox.insert(tk.END, line)

def main():
    """
    Entry point of the application.
    Creates the main Tkinter window and starts the event loop.
    """
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
