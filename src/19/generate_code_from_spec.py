import numpy as np
from PIL import Image

def crop_dark_perimeter(image_path, threshold=50):
    """
    Crops the rows and columns around the perimeter of an image if their mean pixel
    value is below the given threshold.
    
    Args:
        image_path (str): Path to the input image.
        threshold (int): Threshold value for cropping. Rows and columns with mean pixel values
                         below this threshold are removed. Default is 50 (on a scale of 0 to 255).
    
    Returns:
        np.ndarray: Cropped image as a numpy array.
    """
    # Load the image and convert it to grayscale (if not already in grayscale)
    img = Image.open(image_path).convert('L')  # 'L' converts to grayscale
    img_array = np.array(img)

    # Calculate mean values for each row and column
    row_means = img_array.mean(axis=1)
    col_means = img_array.mean(axis=0)

    # Find rows and columns to keep (those with mean values above the threshold)
    rows_to_keep = np.where(row_means > threshold)[0]
    cols_to_keep = np.where(col_means > threshold)[0]

    # Crop the image using the rows and columns to keep
    if len(rows_to_keep) > 0 and len(cols_to_keep) > 0:
        cropped_img = img_array[rows_to_keep[0]:rows_to_keep[-1] + 1, cols_to_keep[0]:cols_to_keep[-1] + 1]
    else:
        # If all rows or columns are below the threshold, return the original image
        cropped_img = img_array

    return cropped_img

# Example usage:
cropped_image_array = crop_dark_perimeter('chicago.jpg', threshold=50)
img = Image.fromarray(cropped_image_array)
img.show()