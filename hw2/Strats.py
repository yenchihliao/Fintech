from trader import Trader
class Naive(Trader):
    # set argment number and limitation
    name = 'naive'
    minArg = []
    MaxArg = []
    arg_count = 0
    # Trade with the strategy
    def __call__(self, data, args):
        pre_price  = 0
        for day in range(len(data)):
            if data[day] > pre_price:
                self.buy(data, day)
            else:
                self.sell(data, day)
            pre_price = data[day]
        return self.final(data)

class Conserv_Lazy(Trader):
    # set argment number and limitation
    name = 'conservLazy'
    minArg = [1]
    MaxArg = [6]
    arg_count = 1
    # Trade with the strategy
    def __call__(self, data, args):
        arg1 = args[0]
        self.buy(data, 0)
        rise4 = 0
        fall4 = 0
        pre_price  = 0
        for day in range(len(data)):
            if data[day] > pre_price:
                rise4+=1
                if rise4 > arg1:
                    rise4 = 0
                    self.buy(data, day)
            else:
                fall4+=1
                if fall4 > arg1:
                    fall4 = 0
                    self.sell(data, day)
            pre_price = data[day]
        #print(self.final(data), arg1)
        return self.final(data)


class Conserv(Trader):
    # set argment number and limitation
    name = 'Conserv'
    minArg = [3]
    MaxArg = [10]
    arg_count = 1
    # Trade with the strategy
    def __call__(self, data, args):
        arg1 = args[0]
        self.buy(data, 0)
        rise4 = 0
        fall4 = 0
        pre_price  = 0
        for day in range(len(data)):
            if data[day] > pre_price:
                rise4 += 1
                fall4 = 0
                if rise4 > arg1:
                    rise4 = 0
                    self.buy(data, day)
            else:
                fall4+=1
                rise4 = 0
                if fall4 > arg1:
                    fall4 = 0
                    self.sell(data, day)
            pre_price = data[day]
        #print(self.final(data), arg1)
        return self.final(data)

class Lazy(Trader):
    name = 'lazy'
    minArg = []
    MaxArg = []
    arg_count = 0
    def __call__(self, data, args):
        self.buy(data, 0)
        self.sell(data, len(data) - 1)
        return self.final(data)

