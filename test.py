from parser import sum_total_expense

import unittest

class TestParserMethods(unittest.TestCase):

  def test_split(self):
      a_dict = {'a':3, 'b':-1}
      self.assertEqual(sum_total_expense(a_dict), 2)

if __name__ == '__main__':
    unittest.main()