import unittest
from datetime import datetime, timedelta
from src.flashcard import Flashcard

class TestFlashcard(unittest.TestCase):
    def setUp(self):
        self.card = Flashcard("What is ML?", "Machine Learning is...", "Fundamentals")
    
    def test_card_creation(self):
        self.assertEqual(self.card.question, "What is ML?")
        self.assertEqual(self.card.answer, "Machine Learning is...")
        self.assertEqual(self.card.category, "Fundamentals")
    
    def test_performance_update(self):
        initial_interval = self.card.interval
        self.card.update_performance(5)  # Perfect recall
        self.assertGreater(self.card.interval, initial_interval)
    
    def test_serialization(self):
        card_dict = self.card.to_dict()
        reconstructed_card = Flashcard.from_dict(card_dict)
        
        self.assertEqual(self.card.question, reconstructed_card.question)
        self.assertEqual(self.card.answer, reconstructed_card.answer)
        self.assertEqual(self.card.category, reconstructed_card.category)

if __name__ == '__main__':
    unittest.main()
