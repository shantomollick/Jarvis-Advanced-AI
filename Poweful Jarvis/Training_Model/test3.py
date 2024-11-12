import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from HEAD.MOUTH import speak

file_path = r"C:\Users\win11\Desktop\Poweful Jarvis\Data\brain_data\data.json"

def load_data(file_path):
    """Load data from a JSON file."""
    try:
        with open(file_path) as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The specified data file was not found.")
        return None

def prepare_training_data(data):
    """Prepare training data from loaded JSON data."""
    training_data = []
    if data:
        for intent in data.get('intents', []):
            if 'patterns' in intent:
                for pattern in intent['patterns']:
                    training_data.append((pattern, intent['tag']))
            else:
                print(f"Warning: 'patterns' key is missing in intent: {intent}")
    return training_data

def train_classifier(training_data):
    """Train the Naive Bayes classifier with the given training data."""
    if not training_data:
        print("Error: No training data found.")
        return None, None

    X, y = zip(*training_data)
    vectorizer = CountVectorizer(ngram_range=(1, 3))
    X_vectorized = vectorizer.fit_transform(X)
    classifier = MultinomialNB()
    classifier.fit(X_vectorized, y)
    return vectorizer, classifier

def get_response(user_input, vectorizer, classifier, data):
    """Generate a response based on user input."""
    if not vectorizer or not classifier:
        return "Error: No training data available to generate a response."

    try:
        user_input_vectorized = vectorizer.transform([user_input])
        predicted_intent = classifier.predict(user_input_vectorized)[0]
        predicted_proba = max(classifier.predict_proba(user_input_vectorized)[0])

        print(f"predicted intent: {predicted_intent}")

        # if predicted_proba < 0.3:
        #     return "I'm not sure I understood that. Could you clarify?"

        for intent in data.get('intents', []):
            if intent.get('tag') == predicted_intent:
                answers = intent.get('responses', [])
                if answers:
                    answer = random.choice(answers)
                    speak(answer)
                    return answers
                else:
                    speak("Sorry, sir")
                    return "I'm sorry, sir. I don't have a response for that."

    except Exception as e:
        print(f"Error processing input: {e}")
        return "Error: Unable to process your request."

# Main execution
def mind(text):
    data = load_data(file_path)
    training_data = prepare_training_data(data)
    vectorizer, classifier = train_classifier(training_data)
    response = get_response(text, vectorizer, classifier, data)
    return response


# while True:
#     text = input("e: ")
#     mind(text)