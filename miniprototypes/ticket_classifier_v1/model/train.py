import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib

DATA_PATH = "data/ticket_data.csv"

# Load and train
df = pd.read_csv(DATA_PATH)
X = df["ticket"]
y = df["category"]
print("Data loaded successfully.")

# Train and save the model
model = make_pipeline(
    TfidfVectorizer(), 
    MultinomialNB()
)
model.fit(X, y)

joblib.dump(model, "./model/ticket_model.joblib")
print("Model trained and saved.")
