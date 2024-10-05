
class CelestialBody:
    def __init__(self, name: str, symbol: str, body):
        self.name = name
        self.symbol = symbol
        self.body = body
        self.altitude = 0
        self.azimuth = 0

    def compute(self, observer):
        self.body.compute(observer)
        self.altitude = self.body.alt
        self.azimuth = self.body.az

    def is_visible(self):
        return self.altitude > 0
