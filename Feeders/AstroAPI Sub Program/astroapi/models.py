class NatalChart:
    def __init__(self, user_id, planets, houses):
        self.user_id = user_id
        self.planets = planets
        self.houses = houses

class TransitData:
    def __init__(self, planet, sign, start_date, end_date):
        self.planet = planet
        self.sign = sign
        self.start_date = start_date
        self.end_date = end_date