from PIL import Image
import os

# Define a function to calculate the difference between two colors
def color_difference(color1, color2):
    """Calculate the difference between two RGB or RGBA colors."""
    # Calculate the absolute difference for each channel
    return sum(abs(component1-component2) for component1, component2 in zip(color1, color2))

threshold = 20

# 设定原始和目标文件夹路径
source_folder = './Art/Building/'
target_folder = './Art/Building_withoutBG/'

# 获取文件夹中所有文件的名字
file_names = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

for file_name in file_names:
    # Load the image
    image_path = os.path.join(source_folder, file_name)
    image = Image.open(image_path)

    # Convert image to RGBA (if not already in this mode)
    image = image.convert("RGBA")

    # Generate a new image with transparent background
    transparent_background = Image.new("RGBA", image.size, (0, 0, 0, 0))
    width, height = image.size

    # Copy pixels from the original image to the new image if they are not the background color
    # Assuming the background is a solid color, we take the color of the top-left pixel as the bg color
    background_color = image.getpixel((0, 0))

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            current_color = image.getpixel((x, y))
            # If the current pixel is NOT the background color, copy it to the new image
            if color_difference(current_color, background_color) > threshold:
                transparent_background.putpixel((x, y), current_color)

    transparent_image_path = os.path.join(target_folder, file_name)
    transparent_background.save(transparent_image_path)
    print(transparent_image_path)



# import cv2
# import numpy as np
# from PIL import Image
# import os

# def find_largest_contour(image):
#     """Find the largest contour in the image."""
#     contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     largest_contour = max(contours, key=cv2.contourArea)
#     return largest_contour

# source_folder = './Art/Building/'
# target_folder = './Art/Building_withoutBG/'

# os.makedirs(target_folder, exist_ok=True)

# file_names = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# for file_name in file_names:
#     image_path = os.path.join(source_folder, file_name)
#     image = Image.open(image_path)
#     image = image.convert("RGBA")

#     # Convert to grayscale
#     gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2GRAY)
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#     # Find the largest contour
#     largest_contour = find_largest_contour(thresh)

#     # Approximate the contour to increase the number of points
#     epsilon = 0.001 * cv2.arcLength(largest_contour, True)
#     approx_contour = cv2.approxPolyDP(largest_contour, epsilon, True)

#     # Calculate the convex hull of the approximated contour
#     convex_hull = cv2.convexHull(approx_contour)

#     # Create a mask for the convex hull
#     mask = np.zeros_like(thresh)
#     cv2.drawContours(mask, [convex_hull], -1, 255, thickness=cv2.FILLED)

#     # Create a new image with transparent background
#     transparent_background = Image.new("RGBA", image.size, (0, 0, 0, 0))
#     width, height = image.size

#     for y in range(height):
#         for x in range(width):
#             if mask[y, x] == 255:  # Pixel is inside the convex hull
#                 transparent_background.putpixel((x, y), image.getpixel((x, y)))

#     transparent_image_path = os.path.join(target_folder, file_name)
#     transparent_background.save(transparent_image_path)
#     print(transparent_image_path)

