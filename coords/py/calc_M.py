# calc_M.py
#   Tomomasa Uchida
#   2020/05/16

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cycler
import matplotlib.gridspec as gridspec
import matplotlib.patches as pat
import cv2
import statistics

# Check arguments
import sys
args = sys.argv
if len(args) != 4:
    print("\nUSAGE   : $ python calc_M.py [input_images_path] [repeat_level] [image_resolution]")
    print("EXAMPLE : $ python calc_M.py LR100/ 100 1000\n")
    sys.exit()



def ReadImage( _img_name ):
    # read input image
    img_BGR = cv2.imread(_img_name)

    # convert color BGR to RGB
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    return img_RGB



def ReadIntermediateImages( _repeat_level, _image_resol, _serial_img_path ):
    # Prepare empty numpy array
    R_pixel_values = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), np.uint8 )
    G_pixel_values = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), np.uint8 )
    B_pixel_values = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), np.uint8 )

    # Read intermediate images
    for i in range( _repeat_level ):
        # Read each ensemble image
        tmp_image_RGB = ReadImage( _serial_img_path + "ensemble"+str(i+1)+".bmp" )

        # Split into RGB and add to numpy array
        R_pixel_values[:,:,i] = tmp_image_RGB[:,:,0] # R
        G_pixel_values[:,:,i] = tmp_image_RGB[:,:,1] # G
        B_pixel_values[:,:,i] = tmp_image_RGB[:,:,2] # B

        if i == _repeat_level-1:
            print("R :", R_pixel_values.shape)
            print("G :", G_pixel_values.shape)
            print("B :", B_pixel_values.shape)

    return R_pixel_values, G_pixel_values, B_pixel_values



def CalcM4EachPixel( _R_pixel_values, _G_pixel_values, _B_pixel_values, _repeat_level, _image_resol ):
    # Set repeat level
    L = _repeat_level
    
    # Set back ground color
    BG_color = [0, 0, 0]

    # Prepare empty numpy array
    #bg_color_indices = np.empty( (_image_resol*1, _image_resol*1, _repeat_level), bool )

    # Get indexes of pixels on which the point color is projected
    idx_point_color = ~((_R_pixel_values == BG_color[0]) & (_G_pixel_values == BG_color[1]) & (_B_pixel_values == BG_color[2]))

    # Calc M for each corresponding pixel
    M_array = np.empty( (_image_resol*1, _image_resol*1), float )
    print("\nCalc M pixel by pixel ...")
    for h in range( _image_resol ):     # height
        for w in range( _image_resol ): # width

            M = 0
            for l in range( L ):
                if idx_point_color[h,w,l] == True:
                    M += 1

            # Save to M array
            M_array[h,w] = M

            # Show progress
            processing_ratio = 100.0 * (float)(h*_image_resol+w) / (float)(_image_resol**2)
            if ( not((h*_image_resol+w) % 100000) and (h*_image_resol+w) > 0 ):
                print(" ", h*_image_resol+w, "pixels done. (", round(processing_ratio,1), "% )")

        # end for w
    # end for h

    M_mean = np.mean(M_array[M_array != 0])
    M_max  = np.max(M_array[M_array != 0])
    M_min  = np.min(M_array[M_array != 0])
    print("\nM_mean :", round(M_mean, 2))
    print("M_max  :", M_max)
    print("M_min  :", M_min, "\n")
    
    return



if __name__ == "__main__":
    # Set repeat level
    repeat_level = int(args[2])
    print("\nRepeat Level     :", repeat_level)

    # Set image resolution
    image_resol = int(args[3])
    print("Image Resolution :", image_resol)

    # Read intermediate images
    serial_img_path = args[1] + "/"
    R_pixel_values, G_pixel_values, B_pixel_values = ReadIntermediateImages( repeat_level, image_resol, serial_img_path )

    # Calc M
    CalcM4EachPixel( R_pixel_values, G_pixel_values, B_pixel_values, repeat_level, image_resol )