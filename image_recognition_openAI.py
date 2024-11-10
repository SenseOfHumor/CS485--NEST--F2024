import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the OpenAI API key
API_KEY = os.getenv("OAPI")

# Initialize the OpenAI client
client = OpenAI(api_key=API_KEY)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/Users/swap/Documents/GitHub/CS485--NEST--F2024/IMG_0520.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)

# Define the prompt
prompt = '''You will see a sample test image with randomly written usernames and passwords.
Your task is to extract the usernames and passwords from the image and return them in a JSON format.
Remember, passwords do not contain spaces.
'''

# Create the messages payload
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }
]

# Call the OpenAI API
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_tokens=500
)

# Extract the response content
result_text = response.choices[0].message.content

print("Response received:", result_text)
