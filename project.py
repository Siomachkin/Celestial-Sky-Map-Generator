from map_generator import MapGenerator
from datetime import datetime
import requests
import re

def main():
    generator = MapGenerator()
    latitude, longitude = get_coordinates()
    current_time = datetime.now()
    visible_bodies = generator.get_visible_bodies(latitude, longitude, current_time)
    generator.create_sky_maps(visible_bodies)
    sky_map = generator.create_combined_sky_map()
    print(sky_map)
    legend = get_legend(visible_bodies)
    print(legend)


def get_coordinates():
    while True:
        auto_detect = input("Auto detect coordinates? (yes/no): ").lower()
        if auto_detect == "yes":
            try:
                latitude, longitude = coordinates_auto_detect()
                print(f"Coordinates: {latitude}, {longitude}")
                return latitude, longitude
            except Exception:
                print("Unable to automatically determine coordinates. Please enter the coordinates manually")
        elif auto_detect == "no":
            return coordinates_user_input()
        else:
            print("Please enter 'yes' or 'no'")


def coordinates_user_input():
        while True:
            latitude = input("Enter your latitude (e.g, 55.7558): ")
            if validate_coordinate(latitude, "latitude"):
                break
        while True:
            longitude = input("Enter your longitude (e.g, 37.6173): ")
            if validate_coordinate(longitude, "longitude"):
                break
        return float(latitude), float(longitude)


def coordinates_auto_detect():
    try:
        response = requests.get("https://ipapi.co/json/")
        data = response.json()
        return float(data["latitude"]), float(data["longitude"])
    except Exception:
        raise ValueError("Failed to determine location")


def validate_coordinate(coord, coord_type):
    if coord_type != "latitude" and coord_type != "longitude":
        return False

    if not re.match(r"^-?\d{1,3}(?:\.\d+)?$", coord):
        print(f"Invalid {coord_type} format. Please try again.")
        return False

    coord_float = float(coord)
    if coord_type == "latitude" and not (-90 <= coord_float <= 90):
        print(f"Latitude must be between -90 and 90 degrees. Please try again.")
        return False
    if coord_type == "longitude" and not (-180 <= coord_float <= 180):
        print(f"Longitude must be between -180 and 180 degrees. Please try again.")
        return False

    return True


def get_legend(bodies):
    legend = ["Legend: "]
    for body in bodies:
        legend.append(f"{body.symbol} - {body.name}")

    return "\n".join(legend)


if __name__ == "__main__":
    main()
