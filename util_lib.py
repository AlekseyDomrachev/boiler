class GeneratorTik():
    def __init__(self, interval):
        self.interval = interval
        self.time_old = 0
        self.out = False

    def tik(self):
        import time
        self.time_new = time.time()
        if self.time_new - self.time_old > self.interval:
            self.time_old = time.time()
            self.out = not self.out
        return self.out


class TriggerRs():
    def __init__(self):
          self.out = False

    def rs(self, set, reset):
        if set:
           self.out = True
        if reset:
           self.out = False
        return self.out


class TriggerRise():
    def __init__(self):
        self.out = False
        self.clk_old = False
    def r_trig(self, clk):
        if clk > self.clk_old:
            self.out = True
        else:
            self.out = False
        if clk != self.clk_old:
            self.clk_old = clk

