# Flask BERT Text Classifier

This project provides a simple Flask API for classifying text using a pre-trained BERT model from Hugging Face's Transformers library. It's designed to offer an easy-to-use interface for NLP tasks such as sentiment analysis, topic classification, and more.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- pip

### Installation

1. Clone the repository to your local machine:

```
git clone [https://github.com/Arkay92/BERTifyAPI](https://github.com/Arkay92/BERTifyAPI.git)
cd your-project-directory
```

## Install the required Python packages:

```
pip install -r requirements.txt
```

## Running the Application
To start the Flask application, run:

```
python app.py
The API will be available at http://localhost:5000.
```

## Using the API
To classify text, send a POST request to /classify with a JSON body containing the text. For example:

```
curl -X POST http://localhost:5000/classify \
-H "Content-Type: application/json" \
-d '{"text": "Your text to classify here"}'
```

You will receive a JSON response with the predicted class:

```
{
  "predicted_class": 1
}
```

## Built With
Flask - The web framework used
Transformers - The library for state-of-the-art machine learning models
PyTorch - The deep learning framework used

## Authors
Robert McMenemy - Creator - Arkay92

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
The incredible Hugging Face team for the Transformers library
The Flask team for making API development a breeze
