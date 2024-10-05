from project import validate_coordinate, coordinates_auto_detect, get_legend
from celestial_body import CelestialBody
import ephem
import emoji
import pytest

def test_validate_coordinates_valid_latitude():
    assert validate_coordinate("45.5", "latitude") == True

def test_validate_coordinates_invalid_latitude():
    assert validate_coordinate("100", "latitude") == False

def test_validate_coordinates_valid_longitude():
    assert validate_coordinate("120", "longitude") == True

def test_validate_coordinates_invalid_longitude():
    assert validate_coordinate("200", "longitude") == False

def test_validate_coordinates_invalid_format():
    assert validate_coordinate("meow", "longitude") == False

def test_validate_coordinates_empty_string():
    assert validate_coordinate("", "longitude") == False

def test_validate_coordinates_boundary_values():
    assert validate_coordinate("-90", "latitude") == True
    assert validate_coordinate("90", "latitude") == True
    assert validate_coordinate("-180", "longitude") == True
    assert validate_coordinate("180", "longitude") == True

def test_validate_coordinates_invalid_second_value():
    assert validate_coordinate("45.5", "meow") == False

def test_coordinates_auto_detect():
    latitude, longitude = coordinates_auto_detect()
    assert isinstance(latitude, float)
    assert isinstance(longitude, float)
    assert -90 <= latitude <= 90
    assert -180 <= longitude <= 180

def test_get_legend():
    celestial_bodies = [
            CelestialBody("Mercury", emoji.emojize(":waning_crescent_moon:"), ephem.Mercury()),
            CelestialBody("Venus", emoji.emojize(":waning_gibbous_moon:"), ephem.Venus()),
            CelestialBody("Mars", emoji.emojize(":orange_circle:"), ephem.Mars()),
            CelestialBody("Jupiter", emoji.emojize(":softball:"), ephem.Jupiter()),
            CelestialBody("Moon", "🌙", ephem.Moon()),
            CelestialBody("Andromeda", "🌌", ephem.readdb("M31,f|G,0:42:44,+41:16:9,3.4,2000"))
    ]

    expected_legend = (
        "Legend: \n"
        "🌘 - Mercury\n"
        "🌖 - Venus\n"
        "🟠 - Mars\n"
        "🥎 - Jupiter\n"
        "🌙 - Moon\n"
        "🌌 - Andromeda"
    )

    result = get_legend(celestial_bodies)
    assert result == expected_legend
