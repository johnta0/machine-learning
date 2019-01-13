#!/usr/bin/env python3

import unittest
import perceptron

class TestPerceptrons(unittest.TestCase):

    def test_NAND(self):
        test_data = [
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        for d in test_data:
            self.assertEqual(d[2], perceptron.NAND(d[0], d[1]))
    
    def test_AND(self):
        test_data = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]
        ]
        for d in test_data:
            self.assertEqual(d[2], perceptron.AND(d[0], d[1]))
    
    def test_OR(self):
        test_data = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        for d in test_data:
            self.assertEqual(d[2], perceptron.OR(d[0], d[1]))

    def test_XOR(self):
        test_data = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        for d in test_data:
            self.assertEqual(d[2], perceptron.XOR(d[0], d[1]))
    
if __name__ == '__main__':
    unittest.main()
