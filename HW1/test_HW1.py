# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


    """
    # Note: This code is completely bogus but demonstrates a few features of python
    # if a == 3 and b == 4 and c == 5:
    #     return 'Right'
    # elif a == 3 and b == c:
    #     return 'Scalene'
    # else:
    #     return 'NotATriangle'

    if not (a+b>c) or not (a+c>b) or not (c+b>a):
        return 'NotATriangle'
    elif pow(a,2) + pow(b,2) == pow(c,2) or pow(a,2) + pow(c,2) == pow(b,2) or pow(c,2) + pow(b,2) == pow(a,2):
        return 'Right'
    elif a == b and b == c:
        return 'Equilateral'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    elif a != b and a != c and b != c:
        return 'Scalene'





def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    # def testSet1(self): # test invalid inputs
    #     # your tests go here.  Include as many tests as you'd like
    #     self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    #
    # def testMyTestSet2(self):
    #     # define multiple test sets to test different aspects of the code
    #     # notice that tests can have bugs too!
    #     self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    #     self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
    #     self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')

    def testNaT(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classifyTriangle(3,1,2),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classifyTriangle(2,3,1),'NotATriangle','Should be NotATriangle')
        self.assertNotEqual(classifyTriangle(2,2,3),'NotATriangle','Should not be NotATriangle')
        self.assertNotEqual(classifyTriangle(2,3,2),'NotATriangle','Should not be NotATriangle')
        self.assertEqual(classifyTriangle(100,600,3000),'NotATriangle','Should be NotATriangle')

    def testRight(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','Should be Right')
        self.assertEqual(classifyTriangle(4,5,3),'Right','Should be Right')
        self.assertEqual(classifyTriangle(5,3,4),'Right','Should be Right')
        self.assertNotEqual(classifyTriangle(6,4,4),'Right','Should not be Right')
        self.assertNotEqual(classifyTriangle(4,4,6),'Right','Should not be Right')
        self.assertEqual(classifyTriangle(5*17,13*17,12*17),'Right','Should be Right')

    def testEq(self):
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','Should be Equilateral')
        self.assertEqual(classifyTriangle(6*3,9+9,36/2),'Equilateral','Should be Equilateral')
        self.assertNotEqual(classifyTriangle(3,2,3),'Equilateral','Should not be Equilateral')
        self.assertNotEqual(classifyTriangle(2,3,3),'Equilateral','Should not be Equilateral')
        self.assertNotEqual(classifyTriangle(3,3,2),'Equilateral','Should not be Equilateral')

    def testIso(self):
        self.assertEqual(classifyTriangle(3,3,2),'Isosceles','Should be Isosceles')
        self.assertEqual(classifyTriangle(2,3,3),'Isosceles','Should be Isosceles')
        self.assertEqual(classifyTriangle(3,2,3),'Isosceles','Should be Isosceles')
        self.assertEqual(classifyTriangle(3*3,pow(3,2),5),'Isosceles','Should be Isosceles')
        self.assertNotEqual(classifyTriangle(4,3,2),'Isosceles','Should not be Isosceles')

    def testSca(self):
        self.assertEqual(classifyTriangle(4,3,2),'Scalene','Should be Scalene')
        self.assertNotEqual(classifyTriangle(3,3,2),'Scalene','Should not be Scalene')
        self.assertNotEqual(classifyTriangle(3,3,3),'Scalene','Should not be Scalene')
        self.assertEqual(classifyTriangle(4*4,3*4,2*4),'Scalene','Should be Scalene')
        self.assertNotEqual(classifyTriangle(pow(3,2),9,pow(7,5)),'Scalene','Should not be Scalene')



if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)

    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
