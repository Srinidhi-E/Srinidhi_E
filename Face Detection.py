import face_recognition
from PIL import Image, ImageDraw

# Use a raw string to avoid unicode escape issues
image_path = r"C:/Users/SRINIDHI/Pictures/group photo.jpg"

# Print the file path to debug
print(f"Loading image from: {image_path}")

try:
    # Load the image file
    image = face_recognition.load_image_file(image_path)
except FileNotFoundError as e:
    print("File not found. Please check the file path:", image_path)
    print(e)
    exit(1)

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

# Convert the image to a PIL Image
pil_image = Image.fromarray(image)

# Create a PIL drawing object to draw on the image
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the image
for (top, right, bottom, left) in face_locations:
    # Draw a rectangle around each face
    draw.rectangle(((left, top), (right, bottom)), outline="red", width=3)

# Display the image
pil_image.show()

# Optionally save the image
output_path = r"C:/Users/SRINIDHI/Pictures/group photo.jpg"

pil_image.save(output_path)
