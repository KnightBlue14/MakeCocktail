import unittest

from MakeCocktails import Ingredient, Spirit

class TestIngredient(unittest.TestCase):
    def test_ingredient(self):
        Ingred1 = Ingredient(5,2,50)
        self.assertEqual(Ingred1.shots, 2,'There are two standard shots')
        self.assertGreater(Ingred1.cost,Ingred1.sum,'The cost is greater than the total revenue')
    def test_spirit(self):
        Spirit1 = Spirit(10,2.5,700,37.5)


if __name__ == '__main__':
    unittest.main()