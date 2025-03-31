import unittest
from unittest.mock import MagicMock, patch
from src.deck import Deck
from src.study_modes import StudyModes
from src.flashcard import Flashcard

class TestStudyModes(unittest.TestCase):
    def setUp(self):
        # Create a deck with sample cards
        self.deck = Deck()
        self.deck.cards = [
            Flashcard("Q1", "A1", "Category1"),
            Flashcard("Q2", "A2", "Category2"),
            Flashcard("Q3", "A3", "Category1")
        ]
        
        # Create study modes instance
        self.study_modes = StudyModes(self.deck)
    
    def test_filter_by_category(self):
        # Test filtering cards by category
        category_cards = self.deck.filter_by_category("Category1")
        self.assertEqual(len(category_cards), 2)
        self.assertTrue(all(card.category == "Category1" for card in category_cards))
    
    @patch('src.study_modes.Prompt.ask')
    @patch('src.study_modes.Confirm.ask')
    def test_study_session_flow(self, mock_confirm, mock_prompt):
        # Mock user interactions
        mock_prompt.return_value = "3"  # Simulating average recall
        mock_confirm.return_value = True  # Continue studying
        
        # Spy on the update_performance method
        with patch.object(Flashcard, 'update_performance') as mock_update:
            # Run a study session
            self.study_modes._study_session(self.deck.cards[:2])
            
            # Verify update_performance was called
            self.assertEqual(mock_update.call_count, 2)
    
    def test_get_due_cards(self):
        # Modify some cards to be due
        for card in self.deck.cards:
            card.next_review = MagicMock(return_value=True)
        
        due_cards = self.deck.get_due_cards()
        self.assertEqual(len(due_cards), 3)

if __name__ == '__main__':
    unittest.main()
