import requests

'''Description: This program translates text from one language 
to another using a translation API. Users can input text and select 
the target language for translation. The program fetches the 
translation and displays it.'''

def translate_text(text, target_language, api_key):
    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
    data = {
        "q": text,
        "target": target_language,
        "format": "text"
    }
    response = requests.post(url, data=data)
    translation = response.json()["data"]["translations"][0]["translatedText"]
    return translation

# Usage example
api_key = "YOUR_GOOGLE_TRANSLATE_API_KEY"
text_to_translate = "Hello, how are you?"
target_language = "fr"  # French
translated_text = translate_text(text_to_translate, target_language, api_key)
print(f"Translation: {translated_text}")
