import cv2
import sys

# Check arguments
args = sys.argv
if len(args) != 3:
    print("\n")
    print("USAGE   : $ python RGB2GRAY.py [input_image_data] [repeat_level]")
    print("EXAMPLE : $ python RGB2GRAY.py ../IMAGE_DATA/RGB/L100.bmp 100 ")
    sys.exit()
    
if __name__ == "__main__":
    # read input image
    img_BGR = cv2.imread(args[1])

    # read repeat level
    repeat_level = args[2]

    # convert color BGR to RGB
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    # convert color RGB to Grayscale
    img_Gray = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2GRAY)

    # convert color RGB to BGR
    # img_in_BGR          = cv2.cvtColor(_img_in_RGB,         cv2.COLOR_RGB2BGR)
    # img_out_BGR         = cv2.cvtColor(_img_adjusted_RGB,  cv2.COLOR_RGB2BGR)
    cv2.imwrite("gray_L" + repeat_level + ".bmp", img_Gray)