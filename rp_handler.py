import json
import random
from PIL import Image, ImageDraw, ImageFont
import os
import string

# Load the JSON file with responses
def load_responses(filename="responses.json"):
    try:
        with open(filename, 'r') as file:
            responses = json.load(file)
        return responses
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {filename}.")
        return {}

# Function to generate a random image
def generate_random_image():
    # Create a blank image with a random color
    width, height = 256, 256
    image = Image.new('RGB', (width, height), color=random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]))
    
    # Add random text to the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # Random text for the image
    text_width, text_height = draw.textsize(text, font=font)
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, fill=(255, 255, 255), font=font)

    # Save the image to a file
    image_filename = "random_image.png"
    image.save(image_filename)
    print(f"Random image saved as {image_filename}")
    image.show()

# Function to get the response based on user input
def get_response(user_input, responses):
    user_input = user_input.lower().strip()  # Normalize input
    return responses.get(user_input, "Sorry, I don't understand that prompt.")

# Main function to interact with the user
def chat():
    responses = load_responses()
    if not responses:
        print("No responses loaded. Exiting...")
        return

    print("Chatbot is ready! Type 'bye' to end the conversation.")
    while True:
        user_input = ("You: create a image")
        
        # Exit the chat if user types 'bye'
        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        # Check for a request for a random image
        if 'image' in user_input.lower() or 'generate' in user_input.lower():
            print("Chatbot: Generating a random image for you!")
            generate_random_image()
        else:
            # Get and print the text-based response
            response = get_response(user_input, responses)
            print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
