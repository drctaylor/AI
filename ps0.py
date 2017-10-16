#!/usr/bin/env python

#Initilize Directories
import cv2
import numpy as np

########################################
# Step 1: Images
#Notes: Color Rectangular images, less than 512 pixels
#Inputs: Images named ps0-1-a-1.png & ps0-1-a-2.png stored in the output folder

#Image 1
img1 = cv2.imread("input/Firefly.png",1)
cv2.imwrite("output/ps0-1-a-1.png", img1)

#Check your image
#cv2.imshow('image',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Image 2
img2 = cv2.imread("input/Woman.png",1)
cv2.imwrite("output/ps0-1-a-2.png", img2)

#Check your image
#cv2.imshow('image',img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

######################################
# Step 2: Color  planes
# Red to Blue Pixels
#   Output: store in Output Folder
    # Image 1 is stored as ps0-2-a-1.png, ps0-2-b-1.png, & ps0-2-c-1.png
    # Image 2 is stored as ps0-2-a-2.png, ps0-2-b-2.png, & ps0-2-c-2.png

#Image 1
img1_blue, img1_green, img1_red = cv2.split(img1)
swapped1 = cv2.merge((img1_red, img1_green, img1_blue))
cv2.imwrite("output/ps0-2-a-1.png", swapped1)
cv2.imwrite("output/ps0-2-b-1.png", img1_green)
cv2.imwrite("output/ps0-2-c-1.png", img1_red)

#Image 2
img2_blue, img2_green, img2_red = cv2.split(img2)
swapped2 = cv2.merge((img2_red, img2_green, img2_blue))
cv2.imwrite("output/ps0-2-a-2.png", swapped2)
cv2.imwrite("output/ps0-2-b-2.png", img2_green) #Monochrome - green channel of image 1
cv2.imwrite("output/ps0-2-c-2.png", img2_red)   #Monochrome - red channel of image 1

#Check your image
#cv2.imshow('image',img1_red)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#######################################
# Step 3: Replacement of pixels 
# Take the inner center square region of 100x100 pixels of monochrome 
# version of image 1 and insert them into the center of monochrome version 
# of image 2

#    Output: Store the new image created as ps0-3-a-1.png in the ouput file
#   Image 1: store as ps0-3-a-1.png

height, width = img1.shape[:2]
x_offset = (width - 100)/2;
y_offset = (height - 100)/2;

img_with_center = img1_green.copy()
center = img2_red[y_offset:y_offset+100, x_offset:x_offset+100]
img_with_center[y_offset:y_offset+100, x_offset:x_offset+100] = center
cv2.imwrite("output/ps0-3-a-1.png", img_with_center)

#Check your image
#cv2.imshow('image',img_with_center)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#######################################
# Step 4: Arithmetic and Geometric operations
# Output: Print out the Min, Max, Mean, and Standard Deviation of the green image
# Store image in Output file

print("Image 1")
# Min
green_min = img1_green.min()
print("Min: ", green_min)

# Max
green_max = img1_green.max()
print("Max: ", green_max)

# Mean
green_mean = img1_green.mean()
print("Mean: ", green_mean)

# Standard deviation
green_std = img1_green.std()
print("Standard deviation: ", green_std)

#Image #2 Information
print("Image 2")
#Min
green_min2 = img2_green.min()
print("Min: ", green_min2)

# Max
green_max2 = img2_green.max()
print("Max: ", green_max2)

# Mean
green_mean2 = img2_green.mean()
print("Mean: ", green_mean2)

# Standard deviation
green_std2 = img2_green.std()
print("Standard deviation: ", green_std2)


# Subtract the mean from all pixels, then divide by standard deviation, 
# then multiply by 10 (if your image is 0 to 255) or by 0.05 
# (if your image ranges from 0.0 to 1.0). Now add the mean back in.
#    Output: ps0-4-b-1.png
# Image 1: store as ps0-4-b-1.png, ps0-4-c-1.png, ps0-4-c-1a.png, & ps0-4-d-1.png
# Image 2: store as ps0-4-b-2.png, ps0-4-c-2.png, ps0-4-c-2a.png, & ps0-4-d-2.png

calculated1 = (img1 - img1.mean()) / img1.std() * 10 + img1.mean()
cv2.imwrite("output/ps0-4-b-1.png", calculated1)

calculated2 = (img2 - img2.mean()) / img2.std() * 10 + img2.mean()
cv2.imwrite("output/ps0-4-b-2.png", calculated2)

#Check your image
#cv2.imshow('image', calculated2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Shift img1_green to the left by 2 pixels.
#    Output: ps0-4-c-1.png

shift_filter = np.float32([[1, 0, -2], [0, 1, 0]])
shifted_green1 = cv2.warpAffine(img1_green, shift_filter, (width, height))
cv2.imwrite("output/ps0-4-c-1.png", shifted_green1)

# filter2D shift
shift_filter = np.zeros((5, 5), np.uint8)
shift_filter[2, 4] = 1
shifted_green1a = cv2.filter2D(img1_green, -1, shift_filter)
cv2.imwrite("output/ps0-4-c-2.png", shifted_green1a)

#Image 2
shift_filter = np.float32([[1, 0, -2], [0, 1, 0]])
shifted_green2 = cv2.warpAffine(img2_green, shift_filter, (width2, height2))
cv2.imwrite("output/ps0-4-c-1a.png", shifted_green2)

# filter2D shift
shift_filter = np.zeros((5, 5), np.uint8)
shift_filter[2, 4] = 1
shifted_green2a = cv2.filter2D(img2_green, -1, shift_filter)
cv2.imwrite("output/ps0-4-c-2a.png", shifted_green2a)

#Check your image
#cv2.imshow('image', shifted_green2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Subtract the shifted version of img1_green from the original, and save the difference image.
#    Output: ps0-4-d-1.png (make sure that the values are legal when you write the image so that you can see all relative differences), text response: What do negative pixel values mean anyways?

# Note: can't just (img1_green - shifted_green) + (shifted_green - img1_green)?
diff1 = np.zeros(img1_green.shape, np.uint8)
for i in range(height):
  for j in range(width):
    if img1_green[i][j] > shifted_green1[i][j]:
      diff1[i][j] = img1_green[i][j] - shifted_green1[i][j]
    else:
      diff1[i][j] = shifted_green1[i][j] - img1_green[i][j]

cv2.imwrite("output/ps0-4-d-1.png", diff1)

diff2 = np.zeros(img2_green.shape, np.uint8)
for i in range(height2):
  for j in range(width2):
    if img2_green[i][j] > shifted_green2[i][j]:
      diff2[i][j] = img2_green[i][j] - shifted_green2[i][j]
    else:
      diff2[i][j] = shifted_green2[i][j] - img2_green[i][j]

cv2.imwrite("output/ps0-4-d-2.png", diff2)
#######################################
# Step 5: Noise

# Take the original colored image (image 1) and start adding Gaussian noise to the pixels in the green channel. Increase sigma until the noise is somewhat visible.
#    Output: 
#   Image 1: ps0-5-a-1.png & ps0-5-b-1.png
noised_green1 = np.array(img1.copy(), dtype=np.float64)
noise = np.random.normal(0, 1, img1_green.shape[:2]) * 7
noised_green1[:, :, 1] += noise
cv2.imwrite('output/ps0-5-a-1.png', noised_green1)

noised_blue1 = np.array(img1.copy(), dtype=np.float64)
noised_blue1[:, :, 0] += noise
cv2.imwrite('output/ps0-5-b-1.png', noised_blue1)


# Now, instead add that amount of noise to the blue channel.
#    Output: ps0-5-b-2.png & ps0-5-b-2.png
noised_green2 = np.array(img2.copy(), dtype=np.float64)
noise = np.random.normal(0, 1, img2_green.shape[:2]) * 7
noised_green2[:, :, 1] += noise
cv2.imwrite('output/ps0-5-a-2.png', noised_green2)

noised_blue2 = np.array(img2.copy(), dtype=np.float64)
noised_blue2[:, :, 0] += noise
cv2.imwrite('output/ps0-5-b-2.png', noised_blue2)