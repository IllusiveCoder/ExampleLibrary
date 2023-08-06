from PIL import Image

'''Create an image resizer tool 
that allows users to resize images to a specified 
width and height. The program will 
use the Python Imaging Library (PIL) to open and manipulate images. Users can provide the path to the image and the desired dimensions, and the program will save the resized image in a new file.'''

def resize_image(input_path, output_path, width, height):
    try:
        image = Image.open(input_path)
        resized_image = image.resize((width, height))
        resized_image.save(output_path)
        print("Image resized and saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Usage example
input_path = "input_image.jpg"
output_path = "output_image.jpg"
width = 300
height = 200
resize_image(input_path, output_path, width, height)