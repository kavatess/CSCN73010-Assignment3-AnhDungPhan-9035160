"""Conversion functions for length, mass and temperature."""

import math

ABSOLUTE_ZERO_C = -273.15
_EPSILON = 1e-9

LENGTH_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
}

MASS_TO_KILOGRAMS = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1.0,
    "oz": 0.028349523125,
    "lb": 0.45359237,
}

TEMPERATURE_UNITS = ("C", "F", "K")


def _convert_by_factor(value, from_unit, to_unit, table):
    if from_unit not in table or to_unit not in table:
        raise ValueError("unsupported unit: %s -> %s" % (from_unit, to_unit))
    return value * table[from_unit] / table[to_unit]


def convert_length(value, from_unit, to_unit):
    """Convert a length between supported units."""
    return _convert_by_factor(value, from_unit, to_unit, LENGTH_TO_METERS)


def convert_mass(value, from_unit, to_unit):
    """Convert a mass between supported units."""
    return _convert_by_factor(value, from_unit, to_unit, MASS_TO_KILOGRAMS)


def _to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    if unit == "K":
        return value - 273.15
    raise ValueError("unsupported temperature unit: %s" % unit)


def _from_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return value * 9 / 5 + 32
    if unit == "K":
        return value + 273.15
    raise ValueError("unsupported temperature unit: %s" % unit)


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between Celsius, Fahrenheit and Kelvin.

    Raises ValueError for NaN values and for temperatures below absolute zero.
    """
    if from_unit not in TEMPERATURE_UNITS or to_unit not in TEMPERATURE_UNITS:
        raise ValueError("unsupported temperature conversion: %s -> %s" % (from_unit, to_unit))
    if math.isnan(value):
        raise ValueError("temperature must be a number")
    celsius = _to_celsius(value, from_unit)
    if celsius < ABSOLUTE_ZERO_C - _EPSILON:
        raise ValueError("temperature is below absolute zero: %g %s" % (value, from_unit))
    return _from_celsius(celsius, to_unit)


def convert(value, from_unit, to_unit):
    """Convert a value, detecting the category from the unit names."""
    if from_unit in LENGTH_TO_METERS and to_unit in LENGTH_TO_METERS:
        return convert_length(value, from_unit, to_unit)
    if from_unit in MASS_TO_KILOGRAMS and to_unit in MASS_TO_KILOGRAMS:
        return convert_mass(value, from_unit, to_unit)
    if from_unit in TEMPERATURE_UNITS and to_unit in TEMPERATURE_UNITS:
        return convert_temperature(value, from_unit, to_unit)
    raise ValueError("cannot convert %s to %s" % (from_unit, to_unit))
