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

BG_COLOR = 0 # Background color : Black(0, 0, 0)

def calc_mean_and_variance(_img_GRAY):
    print("Input image (GRAY)          : ", _img_GRAY.shape) # （height, width, channel）

    # Calc all number of pixels of the input image
    N_all = _img_GRAY.shape[0] * _img_GRAY.shape[1]
    print("Number of pixels            : ", N_all, "(pixels)")

    # Exclude BGColor(Black)
    img_GRAY_non_bgcolor = _img_GRAY[_img_GRAY != BG_COLOR]
    print("Number of NonBGColor pixels : ", img_GRAY_non_bgcolor.shape[0], "(pixels)")

    # NonBGColor_num = np.sum(_img_GRAY != BG_COLOR)
    # print("\nN_all_nonzero: ", NonBGColor_num, "(pixels)")
    # BGColor_num = np.sum(_img_GRAY == BG_COLOR)
    # print("Num of BGColor pixels: ", BGColor_num )
    # print("\ntest:", NonBGColor_num + BGColor_num)

    # print("\nMax :", np.max(_img))
    # print("Min :", np.min(_img))
    print("\nMean:", round(img_GRAY_non_bgcolor.mean(), 2), "(pixel value)")
    print("Var:", round(img_GRAY_non_bgcolor.var(), 2), "((pixel value)^2)")
    print("SD:", round(img_GRAY_non_bgcolor.std(), 2), "(pixel value)")

if __name__ == "__main__":
    img_in_GRAY = cv2.imread(args[1], cv2.IMREAD_GRAYSCALE)
    calc_mean_and_variance(img_in_GRAY)