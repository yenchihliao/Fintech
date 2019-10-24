from trader import Trader
class Naive(Trader):
    # set argment number and limitation
    name = 'naive'
    minArg = []
    MaxArg = []
    gapArg = []
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
    gapArg = [1]
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
    minArg = [3, 1]
    MaxArg = [15, 15]
    gapArg = [1]
    arg_count = 2
    # Trade with the strategy
    def __call__(self, data, args):
        arg1 = args[0]
        arg2 = args[1]
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
                if fall4 > arg2:
                    fall4 = 0
                    self.sell(data, day)
            pre_price = data[day]
        #print(self.final(data), arg1)
        return self.final(data)

class Lazy(Trader):
    name = 'lazy'
    minArg = []
    MaxArg = []
    gapArg = []
    arg_count = 0
    def __call__(self, data, args):
        self.buy(data, 0)
        self.sell(data, len(data) - 1)
        return self.final(data)
    
class RSI(Trader):
    name = 'RSI'
    minArg = [70, 25, 1, 1, 2]
    MaxArg = [100, 60, 50, 40, 25]
    gapArg = [2, 2, 2, 2, 2]
    arg_count = 5
    diffArray = [0]*4000
    isInit = False
    def init(self, data):
        if self.isInit:
            return
        else:
            count = 0
            pre_d = data[0]
            for d in data:
                self.diffArray[count] = d-pre_d
                count += 1
                pre_d = d
            self.isInit = True
    def rsiCal(self, frame, day):
        end = day
        start = max(day-frame, 0)
        smau = []
        smad = []
        for i in range(start, end):
            if self.diffArray[i] > 0:
                smau.append(self.diffArray[i])
            elif self.diffArray[i] < 0:
                smad.append(-1 * self.diffArray[i])
        smau = sum(smau)
        smad = sum(smad)
        if smau == smad == 0:
            smad = 1
            smau = 1
        return smau/(smau+smad) * 100
    def __call__(self, data, args):
        self.init(data)
        tooHot = args[0]
        threshold = args[1]
        lowTre = args[2]
        tooCold = args[3]
        frame = args[4]
        if not (tooHot >= threshold >= lowTre >= tooCold):
            return 10000
        for day in range(len(data)):
            rsi = self.rsiCal(frame, day)
            if rsi >= tooHot:
                self.sell(data, day)
            elif tooHot > rsi >= threshold:
                self.buy(data, day)
            elif threshold > rsi >= lowTre:
                self.hold()
            elif lowTre > rsi >= tooCold:
                self.sell(data, day)
            else:
                self.buy(data, day)
        return self.final(data)

