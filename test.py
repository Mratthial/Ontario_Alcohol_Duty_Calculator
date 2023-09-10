import unittest
import Ontario_Alcohol_Duties

test1_liquor = Ontario_Alcohol_Duties.Liquor('liquor', 'Test_Liquor', 0.75, 0.40, 21.95, 0)
test1_wine = Ontario_Alcohol_Duties.Liquor('wine', 'Test_Wine', 0.75, 0.08, 10.40, 0)

class Test_Liquor_Calculator_Validity(unittest.TestCase):
    def test1_liquor_alcohol_import_duty (self):   
        result = test1_liquor.alcohol_import_duty
        expected_value = 0.0148
        self.assertEqual(result, expected_value)

    def test1_liquor_excise_tax (self):
        result = test1_liquor.excise_tax
        expected_value = 3.5088
        self.assertEqual(result, expected_value)

    def test1_liquor_alcohol_border_levy (self):
        result = test1_liquor.border_levy 
        expected_value = 15.26
        self.assertEquals (result, expected_value)

    def test1_liquor_HST (self):
        result = test1_liquor.HST 
        expected_value = 3.31
        self.assertEquals (result, expected_value)
        
    def test1_liquor_consumer_price (self):
        result = test1_liquor.total_cost
        expected_value = 44.04
        self.assertEquals (result, expected_value)

class Test_Wine_Calculator_Validity(unittest.TestCase):
    def test1_wine_alcohol_import_duty (self):   
        result = test1_wine.alcohol_import_duty
        expected_value = 0.0140
        self.assertEqual(result, expected_value)

    def test1_wine_excise_tax (self):
        result = test1_wine.excise_tax
        expected_value = 0.4650
        self.assertEqual(result, expected_value)

    def test1_wine_alcohol_border_levy (self):
        result = test1_wine.border_levy 
        expected_value = 4.31
        self.assertEquals (result, expected_value)

    def test1_wine_HST (self):
        result = test1_wine.HST 
        expected_value = 1.41
        self.assertEquals (result, expected_value)
        
    def test1_wine_consumer_price (self):
        result = test1_wine.total_cost
        expected_value = 16.60
        self.assertEquals (result, expected_value)

if __name__ == '__main__':
    unittest.main()