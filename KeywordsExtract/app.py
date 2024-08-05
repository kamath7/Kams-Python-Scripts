import nltk
from nltk.tokenize import word_tokenize
import re

nltk.download("punkt")
nltk.download('stopwords')

def extract_keywords(text):
    words = word_tokenize(text)
    service_pattern = re.compile(r'\b\w*Service\b')
    region_pattern = re.compile(r'\b[A-Z]{3}\b')
    error_pattern = re.compile(r'"([^"]+)"')

    keywords = {
        "service": None,
        "region": None,
        "error": None
    }

    for word in words:
        if service_pattern.search(word):
            keywords["service"] = word
        elif region_pattern.search(word):
            keywords["region"] = word
        elif error_pattern.search(word):
            keywords["error"] = error_pattern
    
    return keywords


def print_everything(keywords): #not really necessary. i was just stupid while writing this
    service = keywords["service"]
    region = keywords["region"]
    error = keywords["error"]

    if service and region and error:
        return f"You entered {service}, {region}, {error} "
    else:
        return "I could not find anything"


