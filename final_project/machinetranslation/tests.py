"""System module."""
import unittest
from translator import french_to_english, english_to_french

class Testf2e(unittest.TestCase):
    """ Testf2e """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)


class Teste2f(unittest.TestCase):
    """ Teste2f """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(english_to_french('0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)

unittest.main()

