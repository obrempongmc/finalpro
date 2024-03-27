import requests

def translate_text(text, target_language, subscription_key):
    try:
        # API endpoint URL
        api_url = "https://translation-api.ghananlp.org/v1/translate"
        
        # Request headers
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key
        }
        
        # Request body data
        data = {
            "in": text,
            "lang": target_language
        }
        
        # Send a POST request to the API URL with headers and JSON data
        response = requests.post(api_url, headers=headers, json=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response to JSON format
            translated_data = response.json()
            return translated_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except requests.RequestException as e:
        # If an error occurs during the request, print the error message
        print(f"Error translating text: {e}")
        return None

# Prompt the user to input the text to translate
text_to_translate = input("Enter the text to translate: ")

# Prompt the user to input the target language
target_language = "en-gaa"

# Provide the subscription key
subscription_key ="355b34884c984baeaec3c9e4bd098bef"

# Translate the text
translated_text = translate_text(text_to_translate, target_language, subscription_key)

# Display the translated text if available
if translated_text:
    print("Translated Text:", translated_text)
else:
    print("Failed to translate the text.")