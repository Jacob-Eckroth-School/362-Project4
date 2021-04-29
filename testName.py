import unittest
import genName




class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(genName.createName("Jacob","Eckroth"),"Jacob Eckroth")
    def test2(self):
        self.assertEqual(genName.createName(2,"Eckroth"),None)
    def test_fail(self):
        self.assertEqual(genName.createName("John", "Smith"),"Barack Obama")

if __name__ == "__main__":
    unittest.main()