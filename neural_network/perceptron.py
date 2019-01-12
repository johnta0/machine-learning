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

def test_NAND():
    test_data = [
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
       ]
    for d in test_data:
        if d[2] != NAND(d[0], d[1]):
            return False
    return True
    
if __name__ == '__main__':
    if not test_NAND():
        print("Test failed..")
    else:
        print("Test success!")
