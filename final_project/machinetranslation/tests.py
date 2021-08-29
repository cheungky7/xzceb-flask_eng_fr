import unittest

from translator import englishToFrench,frenchToEnglish

class TestTranslator(unittest.TestCase): 
    def test_englishToFrench_null(self):
        self.assertEqual(englishToFrench(None), None) 

    def test_frenchToEnglish_null(self):
        self.assertEqual(frenchToEnglish(None), None) 
    
    def test_englishToFrench_1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour') 

    def test_frenchToEnglish_1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello') 

if __name__ == '__main__':
    unittest.main()
