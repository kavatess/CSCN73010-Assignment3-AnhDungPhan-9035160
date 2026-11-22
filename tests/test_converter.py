import pytest

from unitconv.converter import convert, convert_length, convert_mass, convert_temperature


def test_length_km_to_mi():
    assert convert_length(10, "km", "mi") == pytest.approx(6.21371, rel=1e-4)


def test_length_identity():
    assert convert_length(5, "m", "m") == 5


def test_mass_kg_to_lb():
    assert convert_mass(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-4)


def test_temperature_c_to_f():
    assert convert_temperature(100, "C", "F") == pytest.approx(212)


def test_temperature_f_to_c():
    assert convert_temperature(32, "F", "C") == pytest.approx(0)


def test_temperature_c_to_k():
    assert convert_temperature(0, "C", "K") == pytest.approx(273.15)


def test_unknown_length_unit_raises():
    with pytest.raises(ValueError):
        convert_length(1, "m", "kg")


def test_unknown_temperature_unit_raises():
    with pytest.raises(ValueError):
        convert_temperature(1, "C", "X")


def test_convert_detects_category():
    assert convert(1, "ft", "in") == pytest.approx(12)
    assert convert(1, "kg", "g") == pytest.approx(1000)


def test_convert_unknown_units_raises():
    with pytest.raises(ValueError):
        convert(1, "foo", "bar")
