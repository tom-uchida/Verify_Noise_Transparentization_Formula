import cv2
import sys
import numpy as np

# Check arguments
args = sys.argv
if len(args) != 5:
    print("\n")
    print("USAGE : $ python calc_mean_var_of_RGB.py [input_image_data] [BGC-R] [BGC-G] [BGC-B]")
    sys.exit()

def calc_mean_of_RGB_value(_img_RGB):
    R, G, B = _img_RGB[:,:,0], _img_RGB[:,:,1], _img_RGB[:,:,2]

    # Get indexes of pixels on which the point color is projected
    idx_point_color = ~((R == BGC_R) & (G == BGC_R) & (B == BGC_R))
    # idx_point_color = R == 255
    num_of_point_color_pixels = np.count_nonzero(idx_point_color)
    print("\nNum. of point color pixels:", num_of_point_color_pixels, "(pixels)")

    mean_R = np.mean(R[idx_point_color])
    mean_G = np.mean(G[idx_point_color])
    mean_B = np.mean(B[idx_point_color])

    print("Mean of R:", round(mean_R, 2), "(pixel value)")
    print("Mean of G:", round(mean_G, 2), "(pixel value)")
    print("Mean of B:", round(mean_B, 2), "(pixel value)\n")

def calc_var_of_RGB_value(_img_RGB):
    R, G, B = _img_RGB[:,:,0], _img_RGB[:,:,1], _img_RGB[:,:,2]

    # Get indexes of pixels on which the point color is projected
    idx_point_color = ~((R == BGC_R) & (G == BGC_G) & (B == BGC_B))
    num_of_point_color_pixels = np.count_nonzero(idx_point_color)
    print("\nNum. of point color pixels:", num_of_point_color_pixels, "(pixels)")

    var_R = np.var(R[idx_point_color])
    var_G = np.var(G[idx_point_color])
    var_B = np.var(B[idx_point_color])

    print("Variance of R:", round(var_R, 2), "(pixel value)^2")
    print("Variance of G:", round(var_G, 2), "(pixel value)^2")
    print("Variance of B:", round(var_B, 2), "(pixel value)^2\n")

if __name__ == "__main__":
    # read input image
    img_BGR = cv2.imread(args[1])

    # convert color BGR to RGB
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    # read back ground color
    BGC_R, BGC_G, BGC_B = int(args[2]), int(args[3]), int(args[4])

    calc_mean_of_RGB_value(img_RGB)
    calc_var_of_RGB_value(img_RGB)