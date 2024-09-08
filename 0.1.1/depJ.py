class glc():
    def __init__(self, v, t, d):
        self.v = v
        self.t = t
        self.d = d
    def vt(self):
        print(self.v * self.t)
    def vd(self):
        print(self.d / self.v)
    def td(self):
        print(self.d / self.t)