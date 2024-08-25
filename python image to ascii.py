from PIL import Image
import numpy as np

def image_to_periods(image_path, max_width=100):
    # Open the image and convert it to grayscale
    img = Image.open(image_path).convert('L')
    
    # Calculate the aspect ratio
    aspect_ratio = img.height / img.width
    
    # Calculate new dimensions while preserving aspect ratio
    if img.width > img.height:
        new_width = max_width
        new_height = int(max_width * aspect_ratio)
    else:
        new_height = max_width
        new_width = int(max_width / aspect_ratio)
    
    # Resize the image
    img = img.resize((new_width, new_height))
    
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Define the characters to use for different shades
    chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    
    # Create the output string
    output = ""
    for row in img_array:
        for pixel in row:
            # Map the pixel value (0-255) to an index in the chars list
            char_index = int(pixel / 255 * (len(chars) - 1))
            output += chars[char_index]
        output += "\n"
    
    return output

# Example usage
image_path = "path/to/your/image.jpg"
result = image_to_periods(image_path, max_width=100)

# Print the result
print(result)

# Optionally, save the result to a file
with open("output.txt", "w") as f:
    f.write(result)
