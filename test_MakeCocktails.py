import unittest

from MakeCocktails import Ingredient, Spirit, Mix

class TestIngredient(unittest.TestCase):
    def test_ingredient(self):
        Ingred1 = Ingredient(5,2,50)
        self.assertEqual(Ingred1.shots, 2,'There are two standard shots')
        self.assertGreater(Ingred1.cost,Ingred1.sum,'The cost is greater than the total revenue')
    def test_exceptions(self):
        try:
            Ingred2 = Ingredient(10,5,0)
        except ZeroDivisionError as exc:
            self.assertRaises(ZeroDivisionError, 'If the volume is zero, it should result in division errors')
    def test_spirit(self):
        Spirit1 = Spirit(10,2.5,700,37.5)
        Spirit2 = Spirit(20,3,700,40)
        self.assertEqual(Spirit1.proof, 75, 'The proof is double the abv')
        self.assertLess(Spirit1.unit_per, 1,'It would be 1 if the abv was 40')
        self.assertLess(Spirit1.unit_per,Spirit2.unit_per, 'Spirit1 has a lower abv')
    def test_mix(self):
        Mix1 = Mix(2,1.5,1000,250)


if __name__ == '__main__':
    unittest.main()