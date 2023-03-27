import unittest
from function import calculate_price

class TestCalculatePrice(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_price("not a dictionary")
        
        with self.assertRaises(ValueError):
            calculate_price({'toppings': 'not a list'})
            
        with self.assertRaises(ValueError):
            calculate_price({'toppings': ['ไข่มุก', 'เฉาก๊วย', 'ถั่วแดง']})
    
    def test_calculate_price(self):
        self.assertEqual(calculate_price({'toppings': ['ไข่มุก']}), 30)
        self.assertEqual(calculate_price({'toppings': ['เฉาก๊วย']}), 35)
        self.assertEqual(calculate_price({'toppings': ['ถั่วแดง']}), 40)
        self.assertEqual(calculate_price({'toppings': ['วิปครีม']}), 40)
        self.assertEqual(calculate_price({'toppings': ['ไข่มุก', 'เฉาก๊วย']}), 40)
        self.assertEqual(calculate_price({'toppings': ['เฉาก๊วย', 'ถั่วแดง']}), 50)
        self.assertEqual(calculate_price({'toppings': ['วิปครีม', 'ถั่วแดง']}), 55)
