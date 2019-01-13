# implment logic circuit by perceptron

def AND(x1, x2):
    w1, w2, threshold = 0.1, 0.1, 0.15 # weight and threshold
    if w1*x1 + w2*x2 > threshold:
        return 1
    return 0

def OR(x1, x2):
    w1, w2, threshold = 1, 1, 0
    if w1*x1 + w2*x2 > threshold:
        return 1
    return 0

def NAND(x1, x2):
    if AND(x1, x2) == 1:
        return 0
    return 1

# XOR can be implement by combination of NAND, OR, AND
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)
