from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity






# loading q&a dataset from text file

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':', 1) for line in lines if ':' in line]
        dataset = [{'question': q, 'answer': a} for q, a in qna_pairs]
    return dataset

# def load_dataset(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#         qna_pairs = []
#         for line in lines:
#             line = line.strip()
#             if ':' in line:
#                 # Split on the first occurrence of ':' only
#                 q, a = line.split(':', 1)
#                 qna_pairs.append((q.strip(), a.strip()))
#         dataset = [{'question': q, 'answer': a} for q, a in qna_pairs]
#     return dataset



# preprocessing the text

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# review the most relevant answer
# def get_answer(question, vectorizer, X, dataset):
#     question = preprocess_text(question)
#     question_vec = vectorizer.transform([question])
#     similarities = cosine_similarity(question_vec, X)
#     best_match_index = similarities.argmax()
#     return dataset[best_match_index]['answer']


def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)

    # Check if the highest similarity score is above a threshold
    threshold = 0.1  # Adjust this value as needed
    best_match_index = similarities.argmax()
    best_similarity = similarities[0, best_match_index]

    if best_similarity < threshold:
        return ""  # Return an empty string if no good match is found

    return dataset[best_match_index]['answer']


# main function
def mind(text):
    dataset_path = r'C:\Users\win11\Desktop\Poweful Jarvis\Data\brain_data\data.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset)
    if not answer or answer == "All suits are fully operational, sir.":
        # print("Jarvis: [No matching response]")
        return None
    # speak(answer)
    # print(f"Jarvis: {answer}")
    return answer

# speak("Welcome sir")
# while True:
#     x = listen()
#     mind(x)

