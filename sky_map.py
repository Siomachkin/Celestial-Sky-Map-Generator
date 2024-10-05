from celestial_body import CelestialBody
import emoji
import wcwidth
import math

class SkyMap:
    def __init__(self, width : int = 100, heigth :int = 30):
        self.width = width
        self.heigth = heigth
        self.sky = [[" " for _ in range(width)] for _ in range(heigth)]


    def add_body(self, body : CelestialBody, direction: str ):
        center_az = {"North" : 0, "East" : math.pi/2, "South" : math.pi, "West" : 3*math.pi/2}
        relative_az = (body.azimuth - center_az[direction] + math.pi) % (2*math.pi) - math.pi
        if -math.pi/2 <= relative_az <= math.pi/2:
            x = int((relative_az /math.pi + 0.5) * (self.width - 2)) + 1;
            y = self.heigth - 2 - int((body.altitude / (math.pi/2)) * (self.heigth - 2)) + 1
            if 0 < x < self.width-1 and 0 < y < self.heigth -1:
                self.sky[y][x] = body.symbol


    def draw_borders(self):
        for i in range(self.width):
            self.sky[0][i] = "-"
            self.sky[-1][i] = "-"

        for j in range(self.heigth):
            shift = 0
            for char in self.sky[j]:
                if wcwidth.wcswidth(char) == 2 and emoji.demojize(char) != ":sun:":
                    shift += 1
            self.sky[j][0] = "|"
            self.sky[j][-1-shift] = "|"

        self.sky[0][0] = self.sky[0][-1] = self.sky[-1][0] = self.sky[-1][-1] = "+"


    def add_title(self, title : str):
        start = (self.width - len(title)) // 2
        for i, char in enumerate(title):
            self.sky[0][start + i] = char


    def render(self):
        return '\n'.join([''.join(row) for row in self.sky])
