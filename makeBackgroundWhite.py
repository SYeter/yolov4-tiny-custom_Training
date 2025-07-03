from PIL import Image
import os
import imghdr
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Set the input and output folder paths
input_folder = 'yolov4-tiny/obj_raw/dataset_jpg'
output_folder = 'yolov4-tiny/obj_raw/dataset_jpg/jpg1'

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
        print(file_path)
        # jpeg_image = cv2.cvtColor(jpeg_image, cv2.COLOR_RGB2BGR)
        # plt.imshow(jpeg_image)
        # plt.show()

        # set the bounds for the green hue
        lower_green = ([74,105,70])
        upper_green = ([80,112,78])
        h = jpeg_image.shape[0] - 1
        w = jpeg_image.shape[1] - 1
        print("img :",jpeg_image[0][0])
        # jpeg_image[0:100, 50:100] = 255,0,0
        cv2.imshow("jpeg_image",jpeg_image)
        # cv2.waitKey(0)
        for y in range(0, h):
            for x in range(0, w):
                print("jpeg_image[y,x] :",list(jpeg_image[y,x]))
                print("lower_green :", lower_green)
                if list(jpeg_image[y,x]) >= lower_green and list(jpeg_image[y,x]) <= upper_green:
                # if list(jpeg_image[y, x]) == [77,113,71]:
                    print("asdasdasdasdas")
                    jpeg_image[y,x] = 255, 255, 255
        cv2.imshow("jpeg_image2", jpeg_image)

        # jpeg_image = image
        # Create the output filename by adding a .dataset_jpg extension
        output_filename = os.path.splitext(filename)[0] + ".dataset_jpg"

        # Save the JPEG image to the output folder
        cv2.imwrite(os.path.join(output_folder, output_filename),jpeg_image)


print("Conversion complete.")