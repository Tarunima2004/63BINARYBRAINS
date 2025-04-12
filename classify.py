from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Training Data
texts = [
    "I need help with my bill",              
    "I was overcharged this month",          
    "Internet is down since yesterday",      
    "WiFi not working at all",               
    "I want to update my email address",     
    "How can I change my password?",         
    "My package has not arrived",            
    "Product delivered was damaged",         
]

labels = [
    "billing",      # First two messages are billing issues
    "billing",
    "technical",    # Next two are technical issues
    "technical",
    "account",      # Next two are account-related
    "account",
    "product",      # Last two are product-related
    "product"
]

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# Predict user message
def classify_issue(message):
    msg_vector = vectorizer.transform([message])
    prediction = model.predict(msg_vector)
    return prediction[0]

# Test
new_msg = "I can't access the internet"
category = classify_issue(new_msg)
print("Predicted category:", category)

joblib.dump(model, "issue_classifier_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")