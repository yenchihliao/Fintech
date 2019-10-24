import numpy as np


def myStrategy(pp, cp, stock):
    # setting param
    if stock == 'DSI':#[79, 31, 31, 25, 5]
        Hot = 96
        threshold = 57
        lowthre = 43
        Cold = 39
        frame = 18
    elif stock == 'IAU':#[94, 55, 19, 16, 5]
        Hot = 92
        threshold = 39
        lowthre = 39
        Cold = 11
        frame = 6
    elif stock == 'LQD':#[94, 40, 37, 25, 17
        Hot = 94
        threshold = 41
        lowthre = 41
        Cold = 27
        frame = 18
    else:
        Hot = 86
        threshold = 53
        lowthre = 43
        Cold = 39
        frame = 18
        
    # input pre_processing
    diffArray = np.zeros(len(pp)+1)
    count = 0
    if len(pp) == 0:
        prePrice = cp
    else:
        prePrice = pp[0]
    for p in pp:
        diffArray[count] = p - prePrice
        count += 1
        prePrice = p

    end = len(pp)
    start = max(end-frame, 0)
    Frame = diffArray[start:end]
    smau = Frame[Frame>0].sum()
    smad = abs(Frame[Frame<0].sum())
    if smau == smad == 0:
        smad = 1
        smau = 1
    rsi = smau/(smau+smad) * 100
    #print(rsi, threshold)
    # play with param
    if rsi >= Hot:
        return -1
    elif Hot > rsi >= threshold:
        return 1
    elif threshold > rsi >= lowthre:
        return 0
    elif lowthre > rsi >= Cold:
        return -1
    else:
        return 1



