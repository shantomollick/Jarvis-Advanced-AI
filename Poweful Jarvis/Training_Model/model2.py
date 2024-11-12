# import json
# import random
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from HEAD.MOUTH import speak
#
# vectorizer = CountVectorizer()
# classifier = MultinomialNB()
#
# with open(r"C:\Users\win11\Desktop\Poweful Jarvis\Data\brain_data\data.json") as file:
#     data = json.load(file)
#
# training_data = []
# for intent in data.get('intent', []):
#     if 'patterns' in intent:
#         for pattern in intent['patterns']:
#             training_data.append((pattern, intent['tag']))
#     else:
#         print(f"Warning: 'patterns' key is missing in intent: {intent}")
#
#
#
# if not training_data:
#     print("Error: No training data found.")
# else:
#     X, y = zip(*training_data)
#     vectorizer.fit_transform(X)
#     classifier.fit(X, y)
#
# def get_response(user_input):
#     user_input_vectorized = vectorizer.transform([user_input])
#
#     predicted_intent = classifier.predict(user_input_vectorized)[0]
#
#     for intent in data.get('intents', []):
#         if intent.get('tag') == predicted_intent:
#             responses = intent.get('responses', [])
#             if responses:
#
#                 return random.choice(responses)
#             else:
#                 return "I'm sorry, sir. I don't have response for that"
#
#
#
# # while True:
# #     x = input("E: ")
# #     y = get_response(x)
# #     speak(y)


import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from HEAD.MOUTH import speak

# Load data from JSON file
try:
    with open(r"C:\Users\win11\Desktop\Poweful Jarvis\Data\brain_data\data.json") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: The specified data file was not found.")
    data = None

# Prepare training data
training_data = []
if data:
    for intent in data.get('intents', []):
        if 'patterns' in intent:
            for pattern in intent['patterns']:
                training_data.append((pattern.lower(), intent['tag']))  # Lowercase patterns
        else:
            print(f"Warning: 'patterns' key is missing in intent: {intent}")

# Global vectorizer and classifier initialization
vectorizer = CountVectorizer()
classifier = MultinomialNB()

# Check for valid training data and fit the model
if not training_data:
    print("Error: No training data found.")
else:
    X, y = zip(*training_data)
    X_vectorized = vectorizer.fit_transform(X)
    classifier.fit(X_vectorized, y)


# Response function
def get_response(user_input):
    # Check if training was successful
    if not training_data:
        return "Error: No training data available to generate a response."

    try:
        # Preprocess the user input (lowercase it)
        user_input = user_input.lower()
        # Vectorize user input
        user_input_vectorized = vectorizer.transform([user_input])
        # Predict the intent
        predicted_intent = classifier.predict(user_input_vectorized)[0]

        # Debug: Print predicted intent to check
        print(f"Predicted intent: {predicted_intent}")

        # Find the corresponding intent and return a random response
        for intent in data.get('intents', []):
            if intent.get('tag') == predicted_intent:
                responses = intent.get('responses', [])
                if responses:
                    res = random.choice(responses)
                    speak(res)
                    return res
                else:
                    return "I'm sorry, sir. I don't have a response for that."

    except Exception as e:
        print(f"Error processing input: {e}")
        return "Error: Unable to process your request."


# Main loop to interact with the assistant
if __name__ == "__main__":
    while True:
        user_input = input("E: ").strip()
        if user_input.lower() == "exit":
            break
        else:
            response = get_response(user_input)
            print(response)
