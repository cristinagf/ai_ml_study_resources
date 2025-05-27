# Ticket classifier v1

A simple prototype to classify tickets (text) into a set of categories:
- "authentication", "email", "hardware", "network", "software", "storage"

The ticket is a line of text.
 
## Data
**CSV**: ticket (text) and label (text)

## Model
Naive Bayes + TF-IDF
Use sklearn

Text Preprocessing: Term Frequency–Inverse Document Frequency. It converts raw text into numerical features based. The result is a sparse vector representing the importance of each word/token.

Classifier (Multinomial Naive Bayes): It's a probabilistic model that assumes features (words) are conditionally independent given the label.For each possible class (e.g., "Login Issue", "Hardware", "Network"), it computes the class given the words, and selects the class with the highest probability.

𝑃(class ∣ words) ∝ 𝑃(class) ∏ 𝑃(word𝑖∣class) 

**Train:** python3 model/train.py

## Prediction Server
**Run:** uvicorn app.main:app --port=5050 --reload

## Send requests

**Manually:**
curl -X POST http://localhost:5050/predict -H "Content-Type: application/json"  -d "{\"text\": \"Can't login to student portal\"}"

**Run script:**
bash ./send_request.sh