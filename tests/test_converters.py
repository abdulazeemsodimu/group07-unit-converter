import pytest
from src.converters import LengthConverter, MassConverter, TemperatureConverter

def test_length_converter():
    converter = LengthConverter()
    assert converter.convert(1, "m", "cm") == 100
    assert converter.convert(1, "km", "m") == 1000

def test_mass_converter():
    converter = MassConverter()
    assert converter.convert(1, "kg", "g") == 1000
    assert converter.convert(1000, "mg", "g") == 1

def test_temperature_converter():
    converter = TemperatureConverter()
    assert converter.convert(0, "C", "F") == 32
    assert pytest.approx(converter.convert(100, "C", "K"), 0.1) == 373.15
