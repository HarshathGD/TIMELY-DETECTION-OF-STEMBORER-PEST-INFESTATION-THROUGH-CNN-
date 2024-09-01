import tensorflow as tf 
classifierLoad = tf.keras.models.load_model('model.h5') # load the model here
import pandas as pd
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw 
from keras.preprocessing import image
test_image1 = cv2.imread('5.jpg',0)
test_image = image.load_img('5.jpg', target_size = (200,200))  # load the sample image here
#test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifierLoad.predict(test_image)
if result[0][0] == 1:
    print("Stemborer larvae ")
    print(" Stage Name : Stemborer larvae Detected ")                
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    
elif result[0][1] == 1:
    print(" Yellow stem  ")
    print(" Stage Name : Yellow stem borer detected ")               
    cv2.imshow('sampleimage',test_image1)
    cv2.waitKey(0)
    

    





