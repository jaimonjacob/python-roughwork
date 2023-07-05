import unittest
from testinput import greet_user

class NamesTestCase(unittest.TestCase):
    '''Test case for testinput.py'''
    def test_first_last_name(self):
        '''Test case for first and last name '''
        formatted_name = greet_user('John', 'Doe')
        self.assertEqual(formatted_name, 'John Doe')

    def test_first_middle_last_name(self):
        '''Test case for first, last and middle name '''
        formatted_name = greet_user('John', 'Doe', 'Henry')
        self.assertEqual(formatted_name, 'John Henry Doe')        

unittest.main()
