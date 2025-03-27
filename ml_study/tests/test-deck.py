import unittest
import os
import tempfile
import pandas as pd
from src.deck import Deck
from src.flashcard import Flashcard

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        
        # Create sample flashcards
        self.card1 = Flashcard("Q1", "A1", "Category1")
        self.card2 = Flashcard("Q2", "A2", "Category2")
        self.deck.add_card(self.card1)
        self.deck.add_card(self.card2)
    
    def test_add_card(self):
        initial_length = len(self.deck.cards)
        new_card = Flashcard("New Q", "New A")
        self.deck.add_card(new_card)
        self.assertEqual(len(self.deck.cards), initial_length + 1)
    
    def test_remove_card(self):
        initial_length = len(self.deck.cards)
        self.deck.remove_card(self.card1.id)
        self.assertEqual(len(self.deck.cards), initial_length - 1)
    
    def test_filter_by_category(self):
        filtered_cards = self.deck.filter_by_category("Category1")
        self.assertEqual(len(filtered_cards), 1)
        self.assertEqual(filtered_cards[0].category, "Category1")
    
    def test_csv_operations(self):
        # Create a temporary file for testing
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
            try:
                # Save to CSV
                self.deck.save_to_csv(temp_file.name)
                
                # Load from CSV
                new_deck = Deck()
                new_deck.load_from_csv(temp_file.name)
                
                # Verify loaded cards
                self.assertEqual(len(new_deck.cards), 2)
            finally:
                # Clean up the temporary file
                os.unlink(temp_file.name)

if __name__ == '__main__':
    unittest.main()
