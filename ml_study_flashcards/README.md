# ML Flashcards Study System

## Project Overview
A comprehensive, flexible flash card system designed for studying Machine Learning concepts, with features for easy customization and learning.

## Features
- Command-line interface for studying
- Spaced repetition learning algorithm
- Multiple study modes (Random, Due Cards, Category Practice)
- Customizable flashcard deck
- Progress tracking

## Prerequisites
- Python 3.8+
- Required libraries:
  - `rich` (for enhanced terminal UI)
  - `pandas` (for data handling)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ml-flashcards.git
cd ml-flashcards
```

2. Create a virtual environment:
```bash
uv venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Usage
- Select study modes from the menu
- Rate your recall after each card
- Track your learning progress

### Running the Flashcard System
```bash
python main.py
```

## Customizing Flashcards
Place your custom CSV in the `data/` directory with columns:
- `question`: The flash card question
- `answer`: The corresponding answer
- `category`: Optional ML category (e.g., "Neural Networks", "Algorithms")
Note the double-quotation boundaries in the provided q/a example file.