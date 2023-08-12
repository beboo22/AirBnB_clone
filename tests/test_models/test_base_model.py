#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
class TestModels(unittest.TestCase):
    def test_baseName(self):
        my_testName = BaseModel()
        my_testName.name = "Beboo"
        self.assertEqual(my_testName.name,"Beboo")
        
    
    def test_baseNum(self):
        my_testNum = BaseModel()
        my_testNum.number = 19
        self.assertEqual(my_testNum.number,19)
    
    def test_baseId(self):
        my_testId = BaseModel()
        my_testId.id = str(uuid4()) 
        self.assertIsInstance(my_testId.id,str)
        self.assertEqual(my_testNum.number,19)



if __name__ == "__main__":
    unittest.main()
