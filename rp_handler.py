import runpod
import time
import requests
import base64
import io
from PIL import Image

def handler(event):
    input = event['input']
    instruction = input.get('instruction')
    #seconds = input.get('seconds', 0)

    # Placeholder for a task; replace with image or text generation logic as needed
    response = requests.post(url, headers=headers, json=instruction)

    if response.status_code == 200:
        result = response.json()

        if result['status'] == 'COMPLETED':
            base64_image = result['output']

            # Remove the data URI prefix
            base64_string = base64_image.split(',')[1]

            # Decode the base64 string
            image_data = base64.b64decode(base64_string)

            # Create an image object from the decoded data
            image = Image.open(io.BytesIO(image_data))

            # Save the image as a PNG file
            image.save('output_image.png', 'PNG')

            print("Image saved as 'output_image.png'")

        else:
            print(f"Request status: {result['status']}")
    else:
        print(f"Request failed with status code: {response.status_code}")

    return result

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
