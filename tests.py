import unittest
from edh_staples import edh_staples
from staple_cards import Staples

# Global variables to use in the tests
test_card1 = Staples("Mana Vault", "Colorless", "Artifact")
test_card2 = Staples("Rampant Growth", "Green", "Sorcery")


class TestStaplesGetsAndSets(unittest.TestCase):
    """Test Staples Getter and Setter Methods"""
    
    def test_get_name(self):
        """Test to verify get_name returns correctly"""
        global test_card1
        
        name = "Mana Vault"
        
        self.assertEqual(test_card1.get_name(), name)
        
    def test_get_color(self):
        """Test to verify get_color returns correctly"""
        global test_card1
        
        color = "Colorless"
        
        self.assertEqual(test_card1.get_color(), color)
        
    def test_get_type(self):
        """test to verify get_type returns correctly"""
        global test_card1
        
        type = "Artifact"
        
        self.assertEqual(test_card1.get_type(), type)
        
    def test_set_name_true(self):
        """Test to verify that set_name returns True"""
        global test_card1
        
        name = "Sol Ring"
        
        self.assertTrue(test_card1.set_name(name))
        
    def test_set_name_sets(self):
        """Test to verify that set_name changes card name"""
        global test_card2
        
        name = "Birds of Paradise"

        test_card1.set_name("Birds of Paradise")
        
        self.assertEqual(test_card1.get_name(), name)
        
    def test_set_color_true(self):
        """Test to verify that set_color returns True"""
        global test_card1
        
        color = "Red"
        
        self.assertTrue(test_card1.set_color(color))
        
    def test_set_color_sets(self):
        """Test to verify that set_color changes the color"""
        global test_card2
        
        color = "Black"
        
        test_card2.set_color("Black")
        
        self.assertEqual(test_card2.get_color(), color)

    def test_set_type_true(self):
        """Test to verify that set_type returns True"""
        global test_card1
        
        cardType = "Creature"
        
        self.assertTrue(test_card1.set_color(cardType))
        
    def test_set_type_sets(self):
        """Test to verify that set_type changes the type"""
        
        global test_card2
        
        cardType = "Instant"
        
        test_card2.set_type(cardType)

        self.assertEqual(test_card2.get_type(), cardType)
        
        
if __name__ == '__main__':
    unittest.main()