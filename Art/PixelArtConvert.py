# Correcting the downsampling approach according to the user's instructions
# Now selecting the median pixel in each 20x20 pixel block.

from PIL import Image
import numpy as np
import os
# from Kmeans import KmeansCluster, Median_Cut

def downsample_image_corrected(image, block_size):
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

BuildingConvert = True
if BuildingConvert:
    # 设定原始和目标文件夹路径
    source_folder = './Art/Building/'
    target_folder = './Art/Building_Correct/'

    # 获取文件夹中所有文件的名字
    file_names = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for file_name in file_names:
        # Load the image
        image_path = os.path.join(source_folder, file_name)
        image = Image.open(image_path)

        print(file_name)

        # Downsample the image using the corrected approach
        image = downsample_image_corrected(image, block_size=2)
        # image = image.convert("RGB")
        # image, cluster_centers = KmeansCluster(image, n_centers = 32)
        # image = Median_Cut(image, num_colors = 64)

        # Save the downsampled image
        downsampled_image_corrected_path = os.path.join(target_folder, file_name)
        image.save(downsampled_image_corrected_path)
        print(downsampled_image_corrected_path)
else:
    # 设定原始和目标文件夹路径
    source_folder = './Art/People/'
    target_folder = './Art/People_Correct/'

    # 获取文件夹中所有文件的名字
    file_names = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for file_name in file_names:
        # Load the image
        image_path = os.path.join(source_folder, file_name)
        image = Image.open(image_path)

        # Downsample the image using the corrected approach
        downsampled_image_corrected = downsample_image_corrected(image, block_size=20)

        # Save the downsampled image
        downsampled_image_corrected_path = os.path.join(target_folder, file_name)
        downsampled_image_corrected.save(downsampled_image_corrected_path)
        print(downsampled_image_corrected_path)