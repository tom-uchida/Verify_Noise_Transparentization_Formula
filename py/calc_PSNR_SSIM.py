from skimage.measure import compare_ssim, compare_psnr
import cv2

# Check arguments
import sys
args = sys.argv
if len(args) != 3:
    sys.exit()

img1 = cv2.imread(args[1], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(args[2], cv2.IMREAD_GRAYSCALE)

print("")
print("PSNR: %f" % compare_psnr(img1, img2))
print("SSIM: %f" % compare_ssim(img1, img2))
print("")