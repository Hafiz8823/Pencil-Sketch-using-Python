# Lord the important Libraries
import numpy as np
import cv2
# Specify the path to lord the Image 

image1 = cv2.imread("bald-eagle.jpg",0) 
window_name = "Original Image"
# Displaying the original image
cv2.imshow(window_name,image1)
# Convert the image from one color to another 
grey_img=cv2.cvtColor(image1,cv2.COLOR_BAYER_BG2GRAY)
invert=cv2.bitwise_not(grey_img)
# Image smoothing
blur=cv2.GaussianBlur(invert,(15,15),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertedblur,scale=256.0)
# Save the converted image in specified path
cv2.imwrite("Sketch.png",sketch)
# Reading an image in default mode
image=cv2.imread("Sketch.png")
# Window name which image is displayed
window_name="Sketch Image"
# Displaying the sketched image 
cv2.imshow(window_name,image)
# Wait for user to press any key 
# (this is necessary to avoid the Python kernel form crashing)
cv2.waitKey(0)
#Closing all windows 
cv2.destroyAllWindows() 
