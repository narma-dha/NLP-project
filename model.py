import pickle
from nltk.tokenize import sent_tokenize
from rouge_score import rouge_scorer

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


def classify_document(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    confidence = max(model.predict_proba(vec)[0])
    return prediction, confidence


def summarize_text(text, n=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:n])


def calculate_rouge(reference, summary):
    scorer = rouge_scorer.RougeScorer(
        ['rouge1', 'rouge2', 'rougeL'], use_stemmer=True
    )
    return scorer.score(reference, summary)
