import unittest
import averageList




class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(averageList.calculateAverage([]),None) #Testing empty list
    def test2(self):
        self.assertEqual(averageList.calculateAverage(["test",1,2,3,4,1.2]),None)   #Testing invalid values
    def test3(self):
        self.assertAlmostEqual(averageList.calculateAverage([1.2,1.3,1.4,2.3,0,5.4,100]),15.942857142857141,3)
    def test4(self):
        self.assertAlmostEqual(averageList.calculateAverage([-1,-3]),-2,3)  #Testing negative numbers
    def test_fail(self):
        self.assertAlmostEqual(averageList.calculateAverage([1,3]),3,3) #fail test

if __name__ == "__main__":
    unittest.main()