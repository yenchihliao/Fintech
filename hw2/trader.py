class Trader():
    def __init__(self):
        self.fund = 10000 # money in pocket
        self.bought = 0 # price when bought
        self.share = 0 # shares holding
    def buy(self, data, day):
        if(not self.bought):
            self.bought = data[day]
            self.share = self.fund//self.bought
            self.fund = self.fund%self.bought
    def sell(self, data, day):
        if(self.bought > 0):
            self.fund += self.share * data[day]
            self.bought = 0
            self.share = 0
            #print('sell on day {}: {}'.format(day, self.fund))
    def hold(self):
          pass
    def final(self, data):
        return self.fund + self.share*data[-1]
    def reset(self):
        self.fund = 10000 # money in pocket
        self.bought = 0 # price when bought
        self.share = 0 # shares holding

