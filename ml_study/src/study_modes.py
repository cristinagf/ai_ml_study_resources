import random
from typing import List, Optional
from rich.console import Console
from rich.prompt import Prompt, Confirm

from src.flashcard import Flashcard
from src.deck import Deck

class StudyModes:
    """
    Implements various study modes for flashcards.
    """
    def __init__(self, deck: Deck):
        """
        Initialize study modes with a given deck.
        
        :param deck: Deck of flashcards to study
        """
        self.deck = deck
        self.console = Console()
    
    def random_mode(self, category: Optional[str] = None):
        """
        Study cards in a random order.
        
        :param category: Optional category to filter cards
        """
        # Filter cards by category if specified
        cards = self.deck.filter_by_category(category)
        
        if not cards:
            self.console.print("[yellow]No cards found to study![/yellow]")
            return
        
        # Shuffle cards
        random.shuffle(cards)
        
        self._study_session(cards)
    
    def due_cards_mode(self):
        """
        Study only cards that are due for review.
        """
        due_cards = self.deck.get_due_cards()
        
        if not due_cards:
            self.console.print("[green]No cards are currently due for review![/green]")
            return
        
        self._study_session(due_cards)
    
    def category_practice_mode(self, category: str):
        """
        Practice a specific category of cards.
        
        :param category: Category to practice
        """
        category_cards = self.deck.filter_by_category(category)
        
        if not category_cards:
            self.console.print(f"[yellow]No cards found in category: {category}[/yellow]")
            return
        
        self._study_session(category_cards)
    
    def _study_session(self, cards: List[Flashcard]):
        """
        Core study session logic.
        
        :param cards: List of flashcards to study
        """
        total_cards = len(cards)
        correct_count = 0
        
        for i, card in enumerate(cards, 1):
            # Clear screen and show progress
            self.console.clear()
            self.console.print(f"[bold]Card {i}/{total_cards}[/bold]")
            self.console.print(f"[cyan]Category: {card.category or 'Uncategorized'}[/cyan]\n")
            
            # Show question
            self.console.print("[bold]Question:[/bold]")
            self.console.print(f"[white]{card.question}[/white]\n")
            
            # Wait for user to reveal answer
            Prompt.ask("[yellow]Press Enter to reveal the answer[/yellow]", show_default=False)
            
            # Show answer
            self.console.print("[bold]Answer:[/bold]")
            self.console.print(f"[white]{card.answer}[/white]\n")
            
            # Get user's self-assessment
            recall_quality = self._get_recall_quality()
            
            # Update card's learning parameters
            card.update_performance(recall_quality)
            
            # Track correct responses
            if recall_quality >= 3:
                correct_count += 1
            
            # Optional: Break between cards
            if i < total_cards:
                continue_studying = Confirm.ask("Continue to next card?", default=True)
                if not continue_studying:
                    break
        
        # Show session summary
        self._show_session_summary(total_cards, correct_count)
    
    def _get_recall_quality(self) -> int:
        """
        Prompt user to rate their recall quality.
        
        :return: Recall quality (0-5)
        """
        while True:
            self.console.print("\n[bold]How well did you remember this card?[/bold]")
            self.console.print("0: Complete blackout")
            self.console.print("1: Incorrect response, forgot most details")
            self.console.print("2: Incorrect response, recalled some details")
            self.console.print("3: Correct response with serious difficulty")
            self.console.print("4: Correct response after some hesitation")
            self.console.print("5: Perfect recall\n")
            
            try:
                quality = Prompt.ask("Enter your recall quality (0-5)", default="3")
                quality = int(quality)
                
                if 0 <= quality <= 5:
                    return quality
                else:
                    self.console.print("[red]Please enter a number between 0 and 5.[/red]")
            except ValueError:
                self.console.print("[red]Invalid input. Please enter a number between 0 and 5.[/red]")
    
    def _show_session_summary(self, total_cards: int, correct_cards: int):
        """
        Display summary of the study session.
        
        :param total_cards: Total number of cards studied
        :param correct_cards: Number of cards recalled correctly
        """
        self.console.print("\n[bold]Study Session Summary[/bold]")
        self.console.print(f"Total Cards Studied: [cyan]{total_cards}[/cyan]")
        self.console.print(f"Correctly Recalled: [green]{correct_cards}[/green]")
        
        # Calculate performance percentage
        performance = (correct_cards / total_cards) * 100 if total_cards > 0 else 0
        self.console.print(f"Performance: [yellow]{performance:.2f}%[/yellow]")

