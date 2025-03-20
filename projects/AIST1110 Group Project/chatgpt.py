import os
import requests
import json
from dotenv import load_dotenv


"""
Note about the API key file location:
Create a hidden file named ".env" in your project folder containing this script.
The content of the hidden file is:
APIM_SUBSCRIPTION_KEY='either one of your primary and seconary API keys'
"""


load_dotenv()

URL = (
    "https://cuhk-api-dev1-apim1.azure-api.net/openai/"
    "deployments/gpt-35-turbo/chat/completions?api-version=2023-05-15"
)

payload = json.dumps({
    "model": "gpt-35-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        },
        {
            "role": "assistant",
            "content": "Hello! How can I assist you today?"            
        },
        {
            "role": "user",
            "content": "Give me 3 MC questions about geography."
        }

    ]
})

headers = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': os.getenv("APIM_SUBSCRIPTION_KEY")
}

response = requests.request("POST", URL, headers=headers, data=payload)

print(response.text)

data = response.json()

print(data['choices'][0]['message']['content'])
