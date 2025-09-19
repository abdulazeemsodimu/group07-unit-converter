class MassConverter:
    units = {"g": 1, "kg": 1000, "mg": 0.001}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Unit not supported")
        in_grams = value * self.units[from_unit]
        return in_grams / self.units[to_unit]


class TemperatureConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = (value - 32) * 5/9
        elif from_unit == "K":
            celsius = value - 273.15
        else:
            raise ValueError("Unit not supported")

        if to_unit == "C":
            return celsius
        elif to_unit == "F":
            return celsius * 9/5 + 32
        elif to_unit == "K":
            return celsius + 273.15
        else:
            raise ValueError("Unit not supported")
