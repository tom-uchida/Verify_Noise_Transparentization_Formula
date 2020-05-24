import cv2
import sys
import numpy as np

# Check arguments
args = sys.argv
if len(args) != 2:
    print("\n")
    print("USAGE   : $ python calc_mean_var.py [input_image_data]")
    print("EXAMPLE : $ python calc_mean_var.py ../IMAGE_DATA/gray_L100.bmp")
    #raise Exception
    sys.exit()

BG_COLOR = [0,0,0]      # Background color : Black(0, 0, 0)
# BG_COLOR = [64,64,64]   # Background color : Gray(64, 64, 64)
print("BGColor                     : ", BG_COLOR)

def calc_mean_and_variance(_img_GRAY):
    print("Input image (GRAY)          : ", _img_GRAY.shape) # （height, width, channel）

    # Calc number of pixels of the input image
    N_all = _img_GRAY.shape[0] * _img_GRAY.shape[1]
    print("Number of pixels            : ", N_all, "(pixels)")

    # Cropping core pixels of the input image
    x_start, x_end = int(_img_GRAY.shape[0]*0.2), int(_img_GRAY.shape[0]*0.8)
    y_start, y_end = int(_img_GRAY.shape[1]*0.2), int(_img_GRAY.shape[1]*0.8)
    img_GRAY_cropped = _img_GRAY[x_start:x_end, y_start:y_end]
    print("\nCropped core pixels of the input image.")
    
    # Exclude BGColor(Black) pixels
    img_GRAY_non_bgcolor = img_GRAY_cropped[img_GRAY_cropped != BG_COLOR[0]]
    print("Number of NonBGColor pixels : ", img_GRAY_non_bgcolor.shape[0], "(pixels)")
    
    print("Mean:", round(img_GRAY_non_bgcolor.mean(), 2), "(pixel value)")
    print("Var:", round(img_GRAY_non_bgcolor.var(), 2), "((pixel value)^2)")
    # print("SD:", round(img_GRAY_non_bgcolor.std(), 2), "(pixel value)")

if __name__ == "__main__":
    img_in_GRAY = cv2.imread(args[1], cv2.IMREAD_GRAYSCALE)
    calc_mean_and_variance(img_in_GRAY)