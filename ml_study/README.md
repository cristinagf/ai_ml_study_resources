# ML Flashcards Study System

## Project Overview
A comprehensive, flexible flash card system designed for studying Machine Learning concepts, with features for easy customization and learning.

## Features
- Command-line interface for studying
- Support for importing custom flashcard sets
- Spaced repetition learning algorithm
- Progress tracking
- Multiple study modes (random, sequential, practice mode)

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
source .venv/bin/activate  #
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Project Structure
```
ml-flashcards/
│
├── src/
│   ├── __init__.py
│   ├── flashcard.py        # Flashcard class definition
│   ├── deck.py             # Deck management
│   ├── study_modes.py      # Different study algorithms
│   └── cli.py              # Command-line interface
│
├── data/
│   └── ml_flashcards.csv   # Default flashcard dataset
│
├── tests/
│   ├── test_flashcard.py
│   ├── test_deck.py
│   └── test_study_modes.py
│
├── requirements.txt
├── README.md
└── main.py                 # Main application entry point
```

## Usage
### Running the Flashcard System
```bash
python main.py
```

### Import Custom Flashcards
Place your custom CSV in the `data/` directory with columns:
- `question`: The flash card question
- `answer`: The corresponding answer
- `category`: Optional ML category (e.g., "Neural Networks", "Algorithms")

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.
