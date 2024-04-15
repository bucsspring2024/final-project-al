class points:
    def __init__(self,multiplier,hits):
        self.multiplier= multiplier
        self.point=0+(hits*multiplier)
    def points(self):
        return self.point