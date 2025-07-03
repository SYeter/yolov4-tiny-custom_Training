from PIL import Image
import os
import imghdr
import cv2
import numpy as np

# Set the input and output folder paths
input_folder = 'dataset'
output_folder = 'yolov4-tiny/obj_raw/dataset_jpg'

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # Check if the file is a regular file and is an image (regardless of extension)
    if os.path.isfile(file_path) and imghdr.what(file_path) is not None:
        # Open and convert the image to JPEG
        jpeg_image = cv2.imread(file_path)
        cv2.resize(jpeg_image,(640,480))
        output_filename = os.path.splitext(filename)[0] + ".dataset_jpg"
        cv2.imshow("jpeg_image", jpeg_image)

        # cv2.waitKey(0)

        # Save the JPEG image to the output folder
        cv2.imwrite(os.path.join(output_folder, output_filename),jpeg_image)
        jpeg_image = cv2.cvtColor(jpeg_image,cv2.COLOR_RGB2BGR)
        print(file_path)

        # set the bounds for the green hue
        lower_green = np.array([0, 0, 100])
        upper_green = np.array([255, 255, 255])

        # create a mask using the bounds set
        mask = cv2.inRange(jpeg_image, lower_green, upper_green)
        # create an inverse of the mask
        mask_inv = cv2.bitwise_not(mask)
        # Filter only the green colour from the original image using the mask(foreground)
        res = cv2.bitwise_not(jpeg_image, jpeg_image, mask=mask)

        cv2.imshow("res", res)
        # cv2.waitKey(0)
        # jpeg_image = image
        # Create the output filename by adding a .dataset_jpg extension



print("Conversion complete.")