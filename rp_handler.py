import requests
import base64
import io
from PIL import Image

# After getting the response from the endpoint
if response.status_code == 200:
    result = response.json()

    if result['status'] == 'COMPLETED':
        base64_image = result['output']

        # Remove the data URI prefix if present
        if ',' in base64_image:
            base64_string = base64_image.split(',')[1]
        else:
            base64_string = base64_image

        # Decode the base64 string
        image_data = base64.b64decode(base64_string)

        # Create an image object from the decoded data
        image = Image.open(io.BytesIO(image_data))

        # Save the image as a PNG file
        image.save('output_image.png', 'PNG')
        
        # Optionally display the image if in a notebook environment
        # from IPython.display import display
        # display(image)

        print("Image saved as 'output_image.png'")
