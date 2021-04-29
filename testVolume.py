import unittest
import volume



class TestCase(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual(volume.volume(1.5,1.5,4),9,3) #Testing floating point volume
    def test2(self):
        self.assertEqual(volume.volume("invalid",1,2),-1)   #Testing for string
    def test3(self):
        self.assertEqual(volume.volume(-1,3,5),-2) #testing for negative size
    def test4(self):
        self.assertEqual(volume.volume(complex(4,3),1,4),-1) #testing for complex number
    def test5(self):
        self.assertAlmostEqual(volume.volume(5,5,5),125,3)  #Testing regular volume

if __name__ == "__main__":
    unittest.main()