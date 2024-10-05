from celestial_body import CelestialBody
from sky_map import SkyMap
from datetime import datetime
import ephem
import emoji

class MapGenerator:
    def __init__(self):
        self.celestial_bodies = [
            CelestialBody("Mercury", emoji.emojize(":waning_crescent_moon:"), ephem.Mercury()),
            CelestialBody("Venus", emoji.emojize(":waning_gibbous_moon:"), ephem.Venus()),
            CelestialBody("Mars", emoji.emojize(":orange_circle:"), ephem.Mars()),
            CelestialBody("Jupiter", emoji.emojize(":softball:"), ephem.Jupiter()),
            CelestialBody("Saturn", emoji.emojize(":ringed_planet:"), ephem.Saturn()),
            CelestialBody("Uranus", emoji.emojize(":ice:"), ephem.Uranus()),
            CelestialBody("Neptune", emoji.emojize(":blue_circle:"), ephem.Neptune()),
            CelestialBody("Sun", emoji.emojize(":sun:"), ephem.Sun()),
            CelestialBody("Moon", "🌙", ephem.Moon()),
            CelestialBody("Andromeda", "🌌", ephem.readdb("M31,f|G,0:42:44,+41:16:9,3.4,2000")),
            CelestialBody("Orion", "🔭", ephem.readdb("M42,f|G,5:35:17,-5:23:28,4,2000")),
            CelestialBody("Pleiades", emoji.emojize(":glowing_star:"), ephem.readdb("M45,f|G,3:47:0,24:07:0,1.2,2000"))
        ]
        self.sky_maps = {}


    def get_visible_bodies(self, latitude, longitude, current_time : datetime):
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.long = str(longitude)
        observer.date = current_time

        visible_bodies = []
        for body in self.celestial_bodies:
            body.compute(observer)
            if body.is_visible():
                visible_bodies.append(body)

        return visible_bodies


    def create_sky_maps(self, bodies):
        directions = ["North", "East", "South", "West"]
        for direction in directions:
            sky_map = SkyMap()
            for body in bodies:
                sky_map.add_body(body, direction)
            sky_map.draw_borders()
            sky_map.add_title(f"{direction} View")
            self.sky_maps[direction] = sky_map.render()


    def create_combined_sky_map(self):
        combined_map = ""
        directions = ["North", "East", "South", "West"]
        for direction in directions:
            if direction in self.sky_maps:
                combined_map += f"\n{self.sky_maps[direction]}\n"

        return combined_map
