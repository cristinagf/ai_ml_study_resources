import csv
import json
import os
from typing import List, Optional
import pandas as pd
from rich.console import Console
from rich.table import Table

from src.flashcard import Flashcard

class Deck:
    """
    Manages a collection of flashcards with various operations.
    """
    def __init__(self, name: str = 'ML Flashcards'):
        """
        Initialize a new deck.
        
        :param name: Name of the deck
        """
        self.name = name
        self.cards: List[Flashcard] = []
        self.console = Console()
    
    def read_csv_with_commas(self, file_path: str):
        """
        Read a CSV file that contains commas within fields using pandas
        
        Args:
            file_path (str): Path to the CSV file
        
        Returns:
            pandas.DataFrame: A DataFrame containing the CSV data
        """
        try:
            # Use pandas read_csv with quoting parameter
            df = pd.read_csv(file_path,
                            quotechar='"',  # Use double quotes to enclose fields
                            quoting=1,      # QUOTE_ALL mode to handle internal commas
                            encoding='utf-8')  # Specify encoding
            
            return df
        
        except FileNotFoundError:
            print("CSV file not found. Please check the file path.")
            return pd.DataFrame()  # Return empty DataFrame if file not found
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return pd.DataFrame()  # Return empty DataFrame on other errors
        
    # def read_csv_with_commas(self, file_path: str):
    #     """
    #     Read a CSV file that contains commas within fields using csv.reader
        
    #     Args:
    #         file_path (str): Path to the CSV file
        
    #     Returns:
    #         list: A list of dictionaries, each representing a row in the CSV
    #     """
    #     qa_data = []
        
    #     # Use csv.reader with the appropriate dialect
    #     with open(file_path, 'r', encoding='utf-8') as csvfile:
    #         # Use csv.reader with quoting to handle commas within fields
    #         csv_reader = csv.reader(csvfile, quotechar='"', delimiter=',', 
    #                                 quoting=csv.QUOTE_ALL, skipinitialspace=True)
            
    #         # Assuming the first row is a header
    #         headers = next(csv_reader)
            
    #         # Read the rest of the rows
    #         for row in csv_reader:
    #             # Create a dictionary mapping headers to row values
    #             qa_entry = dict(zip(headers, row))
    #             qa_data.append(qa_entry)
        
    #     return qa_data

    def load_from_csv(self, filepath: str):
        """
        Load flashcards from a CSV file.
        
        :param filepath: Path to the CSV file
        """
        try:
            # Use pandas for robust CSV reading
            # df = pd.read_csv(filepath, keep_default_na=False)
            df = self.read_csv_with_commas(filepath)
            
            # Validate required columns
            required_columns = ['question', 'answer']
            for col in required_columns:
                if col not in df.columns:
                    raise ValueError(f"Missing required column: {col}")
            
            # Convert to flashcards
            self.cards = [
                Flashcard(
                    question=row['question'],
                    answer=row['answer'],
                    category=row.get('category', '')
                ) for _, row in df.iterrows()
            ]
            
            self.console.print(f"[green]Loaded {len(self.cards)} flashcards from {filepath}[/green]")
        except Exception as e:
            self.console.print(f"[red]Error loading CSV: {e}[/red]")
            raise
    
    def save_to_csv(self, filepath: str):
        """
        Save current deck to a CSV file.
        
        :param filepath: Path to save the CSV file
        """
        try:
            # Convert cards to dictionaries
            card_dicts = [card.to_dict() for card in self.cards]
            
            # Create DataFrame and save
            df = pd.DataFrame(card_dicts)
            df.to_csv(filepath, index=False)
            
            self.console.print(f"[green]Saved {len(self.cards)} flashcards to {filepath}[/green]")
        except Exception as e:
            self.console.print(f"[red]Error saving CSV: {e}[/red]")
            raise
    
    def add_card(self, card: Flashcard):
        """
        Add a new flashcard to the deck.
        
        :param card: Flashcard to add
        """
        self.cards.append(card)
    
    def remove_card(self, card_id: str):
        """
        Remove a card from the deck by its ID.
        
        :param card_id: Unique identifier of the card to remove
        """
        self.cards = [card for card in self.cards if card.id != card_id]
    
    def get_due_cards(self) -> List[Flashcard]:
        """
        Get cards that are due for review.
        
        :return: List of due flashcards
        """
        return [card for card in self.cards if card.is_due()]
    
    def filter_by_category(self, category: Optional[str] = None) -> List[Flashcard]:
        """
        Filter cards by category.
        
        :param category: Category to filter by. If None, return all cards.
        :return: Filtered list of flashcards
        """
        if not category:
            return self.cards
        return [card for card in self.cards if card.category.lower() == category.lower()]
    
    def display_deck_summary(self):
        """
        Display a summary of the deck using rich tables.
        """
        table = Table(title="Deck Summary")
        table.add_column("Category", style="cyan")
        table.add_column("Total Cards", style="magenta")
        table.add_column("Due Cards", style="red")
        
        # Group cards by category
        category_groups = {}
        for card in self.cards:
            category = card.category or "Uncategorized"
            if category not in category_groups:
                category_groups[category] = []
            category_groups[category].append(card)
        
        # Add rows to the table
        for category, cards in category_groups.items():
            due_cards = [card for card in cards if card.is_due()]
            table.add_row(
                category, 
                str(len(cards)), 
                str(len(due_cards))
            )
        
        self.console.print(table)
