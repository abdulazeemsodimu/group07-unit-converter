class LengthConverter:
    """
    Handles conversion between length units.

    Supported units:
        - "m"  : meter (base unit)
        - "km" : kilometer
        - "cm" : centimeter
        - "mm" : millimeter
    """

    units = {
        "m": 1,        # meter
        "km": 1000,    # kilometer
        "cm": 0.01,    # centimeter
        "mm": 0.001,   # millimeter
    }

    def convert(self, value, from_unit, to_unit):
        """
        Convert a length value from one unit to another.

        Args:
            value (float): The numerical value to be converted.
            from_unit (str): The unit of the input value. Must be one of: "m", "km", "cm", "mm".
            to_unit (str): The unit to convert the value into. Must be one of: "m", "km", "cm", "mm".

        Returns:
            float: Converted value in the target unit.

        Raises:
            ValueError: If either `from_unit` or `to_unit` is not supported.
        """
        
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Unit not supported")

        # Convert input value to meters (base unit)
        in_meters = value * self.units[from_unit]

        # Convert from meters to target unit
        return in_meters / self.units[to_unit]

class MassConverter:
    """
    Handles conversion between mass units.

    Supported units:
        - "g"  : gram (base unit)
        - "kg" : kilogram
        - "mg" : milligram
    """
    
    units = {"g": 1, "kg": 1000, "mg": 0.001}

    def convert(self, value, from_unit, to_unit):
        """
        Convert a mass value from one unit to another.

        Args:
            value (float): The numerical value to be converted.
            from_unit (str): The unit of the input value. Must be one of: "g", "kg", "mg".
            to_unit (str): The unit to convert the value into. Must be one of: "g", "kg", "mg".

        Returns:
            float: Converted value in the target unit.

        Raises:
            ValueError: If either `from_unit` or `to_unit` is not supported.
        """
        
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Unit not supported")

        # Convert input value to grams (base unit)
        in_grams = value * self.units[from_unit]

        # Convert from grams to target unit
        return in_grams / self.units[to_unit]

class TemperatureConverter:
    """Handles conversion between Celsius, Fahrenheit, Kelvin"""

    def convert(self, value, from_unit, to_unit):
        """Convert temperature from one unit to another."""
        # Convert input to Celsius first
        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = (value - 32) * 5/9
        elif from_unit == "K":
            celsius = value - 273.15
        else:
            raise ValueError("Unit not supported")

        # Convert from Celsius to target
        if to_unit == "C":
            return celsius
        elif to_unit == "F":
            return celsius * 9/5 + 32
        elif to_unit == "K":
            return celsius + 273.15
        else:
            raise ValueError("Unit not supported")

