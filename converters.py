class Main:
    def __init__(self, magnitude, unit):
        self.magnitude = magnitude
        self.type = unit.lower()


class Kg_Lb(Main):
    def covert(self):
        if self.type == 'kg':
            print(self.magnitude * 2.205)

        if self.type == 'lbs':
            print(self.magnitude / 2.205)


class Li_Ga(Main):
    def convert(self):
        if self.type == 'li':
            print(str(self.magnitude / 3.785) + ' ga')

        if self.type == 'ga':
            print(str(self.magnitude * 3.785) + ' li')


class Km_Mi(Main):
    def convert(self):
        if self.type == 'km':
            print(str(self.magnitude / 1.609) + ' mi')

        if self.type == 'mi':
            print(str(self.magnitude * 1.609) + ' km' )





