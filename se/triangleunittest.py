import unittest

def check_triangle(a, b, c):
   
    if a <= 0 or b <= 0 or c <= 0:
        return False
        
   
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

class TestCheckTriangle(unittest.TestCase):

    def test_valid_triangle(self):
      
        self.assertTrue(check_triangle(3, 4, 5))

    def test_degenerate_triangle(self):
        
        self.assertFalse(check_triangle(1, 2, 3))

    def test_invalid_triangle(self):
        
        self.assertFalse(check_triangle(10, 2, 2))

    def test_zero_side_triangle(self):
        
        self.assertFalse(check_triangle(0, 5, 5))

    def test_negative_side_triangle(self):
       
        self.assertFalse(check_triangle(-3, 4, 5))

if _name_ == '_main_':
    unittest.main()