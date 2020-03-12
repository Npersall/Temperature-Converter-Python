

class TempConverter(object):

    def to_celsius(self, far):
        return (far -32) * 5 / 9

    def to_fahrenheiht(self, cel):
        return (((cel / 5) * 9) + 32.0)