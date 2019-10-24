#import sys
#print(sys.executable)
import sys
import matplotlib.pyplot as plt
from Strats import Lazy, Naive, Conserv_Lazy, Conserv, RSI
class Evaluate:
    pw = [100000000, 1000000, 10000, 100]
    maxVal = 0
    maxArg = []
    def __init__(self, cls, data):
        self.cls = cls
        self.data = data
    def ReturnRate(self, args):
        ret = self.cls(self.data, args)
        self.cls.reset()
        print("with:", args, ret)
        return ret
    def loopOver(self, Layer, args):
        if(Layer >= self.cls.arg_count):
            tmp = self.ReturnRate(args)
            if tmp > self.maxVal:
                print("###MaxFound")
                self.maxVal = tmp
                self.maxArg = args[:]
            if tmp == self.maxVal:
                print('***Even')
            return
        for i in range(self.cls.minArg[Layer], self.cls.MaxArg[Layer], self.cls.gapArg[Layer]):
            args[Layer] = i
            self.loopOver(Layer+1, args)
    def FindOptArgs(self):
        self.loopOver(0, [0]*self.cls.arg_count)
        return self.maxVal, self.maxArg
    
    def name(self):
        return self.cls.name
# Process input
#DSI, IAU, LQD, SPY
files = ['DSI.csv','IAU.csv', 'LQD.csv', 'SPY.csv']
for file in files:
    print('processing:', file)
    f = open(file, 'r')
    closeP = []
    i = 0
    f.readline()
    while(True):
        line = f.readline()
        if not line:
            break
        closeP.append(float(line.split(',')[5]))
    s = RSI()
    e = Evaluate(s, closeP)
    print(e.name(), e.FindOptArgs(), file)
    #plt.plot(closeP, label=file)
    #plt.show()
