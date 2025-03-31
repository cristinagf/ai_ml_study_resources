from dataclasses import dataclass, field
from datetime import datetime, timedelta
import uuid

@dataclass
class Flashcard:
    """
    Represents a single flashcard with spaced repetition learning properties.
    """
    question: str
    answer: str
    category: str = ''
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    # Spaced Repetition Tracking
    easiness_factor: float = 2.5
    interval: int = 0
    repetitions: int = 0
    next_review: datetime = field(default_factory=datetime.now)
    
    def update_performance(self, quality: int):
        """
        Update card's learning parameters based on recall quality.
        
        :param quality: 0-5 scale of how well the card was remembered
            0: Complete blackout
            1: Incorrect response, forgot most details
            2: Incorrect response, recalled some details
            3: Correct response with serious difficulty
            4: Correct response after some hesitation
            5: Perfect recall
        """
        # Ensure quality is within 0-5 range
        quality = max(0, min(5, quality))
        
        # Update easiness factor
        self.easiness_factor = max(1.3, self.easiness_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        
        # Adjust repetition and interval
        if quality < 3:
            # Reset learning if performance is poor
            self.repetitions = 0
            self.interval = 0
        else:
            self.repetitions += 1
            
            # Calculate new interval based on repetitions
            if self.repetitions == 1:
                self.interval = 1
            elif self.repetitions == 2:
                self.interval = 6
            else:
                self.interval = round(self.interval * self.easiness_factor)
        
        # Set next review date
        self.next_review = datetime.now() + timedelta(days=self.interval)
        
        return self.interval

    def is_due(self) -> bool:
        """
        Check if the flashcard is due for review.
        
        :return: Boolean indicating if the card should be reviewed
        """
        return datetime.now() >= self.next_review

    def to_dict(self) -> dict:
        """
        Convert flashcard to a dictionary for easy serialization.
        
        :return: Dictionary representation of the flashcard
        """
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'easiness_factor': self.easiness_factor,
            'interval': self.interval,
            'repetitions': self.repetitions,
            'next_review': self.next_review.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Flashcard instance from a dictionary.
        
        :param data: Dictionary containing flashcard data
        :return: Flashcard instance
        """
        card = cls(
            question=data['question'],
            answer=data['answer'],
            category=data.get('category', '')
        )
        card.id = data.get('id', str(uuid.uuid4()))
        card.easiness_factor = data.get('easiness_factor', 2.5)
        card.interval = data.get('interval', 0)
        card.repetitions = data.get('repetitions', 0)
        card.next_review = datetime.fromisoformat(data.get('next_review', datetime.now().isoformat()))
        
        return card
