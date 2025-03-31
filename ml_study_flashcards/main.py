import os
import sys
from typing import Optional

# Ensure the project root is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

from src.deck import Deck
from src.study_modes import StudyModes

def main():
    """
    Main application entry point for ML Flashcards.
    """
    console = Console()
    console.print(Panel.fit("[bold cyan]ML Flashcards Study System[/bold cyan]", border_style="blue"))
    
    # Initialize deck
    deck = Deck()
    
    # Try to load default dataset
    default_dataset = os.path.join('data', 'ml_flashcards.csv')
    try:
        deck.load_from_csv(default_dataset)
    except Exception as e:
        console.print(f"[yellow]Could not load default dataset: {e}[/yellow]")
        load_manual = Confirm.ask("Would you like to manually add cards?")
        if not load_manual:
            console.print("[red]Exiting application.[/red]")
            return
    
    # Create study modes instance
    study_modes = StudyModes(deck)
    
    while True:
        console.clear()
        console.print("[bold]ML Flashcards Menu:[/bold]")
        console.print("1. View Deck Summary")
        console.print("2. Random Study Mode")
        console.print("3. Due Cards Study Mode")
        console.print("4. Category Practice Mode")
        console.print("5. Save Current Progress")
        console.print("6. Exit")
        
        choice = Prompt.ask("Select an option", choices=['1', '2', '3', '4', '5', '6'])
        
        if choice == '1':
            # View deck summary
            deck.display_deck_summary()
            Prompt.ask("Press Enter to continue")
        
        elif choice == '2':
            # Random study mode
            category = Prompt.ask("Enter category to study (or press Enter for all)", default='')
            study_modes.random_mode(category or None)
        
        elif choice == '3':
            # Due cards mode
            study_modes.due_cards_mode()
        
        elif choice == '4':
            # Category practice mode
            unique_categories = list(set(card.category for card in deck.cards if card.category))
            console.print("\nAvailable Categories:")
            for i, cat in enumerate(unique_categories, 1):
                console.print(f"{i}. {cat}")
            
            category_choice = Prompt.ask("Select a category number", 
                                          choices=[str(i) for i in range(1, len(unique_categories)+1)])
            category = unique_categories[int(category_choice) - 1]
            study_modes.category_practice_mode(category)
        
        elif choice == '5':
            # Save progress
            save_path = os.path.join('data', 'ml_flashcards_progress.csv')
            deck.save_to_csv(save_path)
            console.print(f"[green]Progress saved to {save_path}[/green]")
            Prompt.ask("Press Enter to continue")
        
        elif choice == '6':
            # Exit
            save_prompt = Confirm.ask("Do you want to save your progress before exiting?")
            if save_prompt:
                save_path = os.path.join('data', 'ml_flashcards_progress.csv')
                deck.save_to_csv(save_path)
            console.print("[bold green]Keep studying and practicing![/bold green]")
            break

if __name__ == "__main__":
    main()

