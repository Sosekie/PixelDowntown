# Correcting the downsampling approach according to the user's instructions
# Now selecting the median pixel in each 20x20 pixel block.

from PIL import Image
import numpy as np

def downsample_image_corrected(image, block_size=20):
    # Convert image to numpy array
    img_array = np.array(image)
    
    # Calculate the number of blocks in each dimension
    num_blocks_x = img_array.shape[1] // block_size
    num_blocks_y = img_array.shape[0] // block_size
    
    # Create an empty array for the downsampled image
    downsampled_array = np.zeros((num_blocks_y, num_blocks_x, img_array.shape[2]), dtype=img_array.dtype)
    
    # Iterate through each block and select the median pixel
    for y in range(num_blocks_y):
        for x in range(num_blocks_x):
            # Extract the block
            block = img_array[y*block_size:(y+1)*block_size, x*block_size:(x+1)*block_size]
            # Find the median pixel
            median_pixel = np.median(block.reshape(-1, block.shape[2]), axis=0)
            downsampled_array[y, x] = median_pixel
    
    # Convert the downsampled array to an image
    downsampled_image = Image.fromarray(downsampled_array.astype(np.uint8))
    return downsampled_image

for i in range(3):
    # Load the image
    image_path = './Art/Building/'+str(i+1)+'.png'
    image = Image.open(image_path)

    # Downsample the image using the corrected approach
    downsampled_image_corrected = downsample_image_corrected(image)

    # Save the downsampled image
    downsampled_image_corrected_path = './Art/Building_Correct/'+str(i+1)+'.png'
    downsampled_image_corrected.save(downsampled_image_corrected_path)

    # Display the downsampled image
    downsampled_image_corrected.show()