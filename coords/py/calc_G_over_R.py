import cv2
import sys
import numpy as np

# Check arguments
args = sys.argv
if len(args) != 2:
    print("\n")
    print("USAGE : $ python calc_G_over_R.py [input_image_data]")
    sys.exit()

# When the background color is "black"
def calc_G_over_R(_img_RGB):
    R, G, B = _img_RGB[:,:,0], _img_RGB[:,:,1], _img_RGB[:,:,2]

    # Get indexes of pixels on which the point color is projected
    idx_point_color = ~((R == 0) & (G == 0) & (B == 0))
    # idx_point_color = R == 255
    num_of_point_color_pixels = np.count_nonzero(idx_point_color)
    print("\nNum. of point color pixels:", num_of_point_color_pixels, "(pixels)")

    # Calc G/R
    G_over_R = G[idx_point_color] / R[idx_point_color]
    # print("test:", G_over_R[:10])

    # Calc mean of G/R
    mean_G_over_R = np.mean(G_over_R)
    print("Mean of G/R:", round(mean_G_over_R, 4), "(pixel value)")

    # Calc variance of G/R
    var_G_over_R = np.var(G_over_R)
    print("Variance of G/R:", round(var_G_over_R, 4), "(pixel value)^2\n")

if __name__ == "__main__":
    # read input image
    img_BGR = cv2.imread(args[1])

    # convert color BGR to RGB
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    calc_G_over_R(img_RGB)