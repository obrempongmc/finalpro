import requests

def convert_text_to_speech(text, language, subscription_key):
    try:
        # API endpoint URL for text-to-speech
        api_url = "https://translation-api.ghananlp.org/tts/v1/tts"
        
        # Request headers
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key
        }
        
        # Request body data
        data = {
            "text": text,
            "language": language
        }
        
        # Send a POST request to the API URL with headers and JSON data
        response = requests.post(api_url, headers=headers, json=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the audio content received in the response
            return response.content
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except requests.RequestException as e:
        # If an error occurs during the request, print the error message
        print(f"Error converting text to speech: {e}")
        return None

# Example usage:
text_to_convert = "Wubebu ɔkyerɛkyerɛfo yi dɛn?"
language = "tw"
subscription_key = "355b34884c984baeaec3c9e4bd098bef"

audio_content = convert_text_to_speech(text_to_convert, language, subscription_key)

if audio_content:
    # Save the audio content to a file
    with open("output_audio.wav", "wb") as audio_file:
        audio_file.write(audio_content)
    print("Text converted to speech successfully. Audio saved as output_audio.wav")
else:
    print("Failed to convert text to speech.")
