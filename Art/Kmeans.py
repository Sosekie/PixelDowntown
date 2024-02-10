from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
from typing import Tuple

def KmeansCluster(image: Image.Image, n_centers: int) -> Tuple[Image.Image, np.ndarray]:
    """
    Perform K-means clustering on an image and return the clustered image and cluster centers.

    Parameters:
    image (Image.Image): The input image to cluster.
    n_centers (int): The number of clusters to form.

    Returns:
    Image.Image: The clustered image.
    np.ndarray: The array of cluster centers.
    """
    # Convert image data to a list of RGB tuples
    img_data = np.array(image)
    pixels = img_data.reshape((-1, 3))
    
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=n_centers, random_state=0).fit(pixels)
    
    # Retrieve the cluster centers and labels
    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # Map each pixel to the cluster center
    clustered_data = cluster_centers[labels].astype('uint8')
    # Reshape data to the original image dimensions
    clustered_image = clustered_data.reshape(img_data.shape)
    
    # Convert back to an image
    clustered_img = Image.fromarray(clustered_image)
    
    return clustered_img, cluster_centers

def Median_Cut(cluster_image, num_colors):
    cluster_image = cluster_image.convert("RGB")
    cluster_image = cluster_image.quantize(colors=num_colors, method=Image.MEDIANCUT)
    cluster_image = cluster_image.convert("RGBA")
    return cluster_image

# for i in range(1):
#     # Load the image
#     image_path = './Art/Building/'+'bakery_1'+'.png'
#     image = Image.open(image_path)
#     image = image.convert("RGB")

#     cluster_image, cluster_centers = KmeansCluster(image, n_centers = 64)

#     MedianCut = False
#     if MedianCut:
#         cluster_image = Median_Cut(cluster_image, num_colors = 24)

#     cluster_image_path = './Art/Building_Correct/'+'bakery_1'+'.png'
#     cluster_image.save(cluster_image_path)

#     print(cluster_image_path)