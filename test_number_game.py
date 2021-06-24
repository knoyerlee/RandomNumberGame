import unittest
from number_game import NumbersGame

class TestingNumbersGame(unittest.TestCase):
    def setUp(self):
        self.ng = NumbersGame()
        self.user_number = '33'
        self.pc_number = 23

    def test_prompt_user(self):
       self.assertEquals(self.user_number, '33')
    
    def test_compare_nums_greater(self):
        self.user_number = int(self.user_number)
        self.assertGreater(self.user_number, self.pc_number)

    def test_compare_nums_lesser(self):
        self.user_number = 13
        self.assertLess(self.user_number, self.pc_number)

    def test_compare_nums_equals(self):
        self.user_number = 23
        self.assertEqual(self.user_number, self.pc_number)

if __name__ == '__main__':
    unittest.main()
