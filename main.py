from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

def classify_text(text):
    """
    Classify the input text and return the predicted class.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    return predicted_class_id

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Classify the text
    predicted_class_id = classify_text(text)

    # Return the classification result
    return jsonify({'predicted_class': predicted_class_id})

if __name__ == '__main__':
    app.run(debug=True)
