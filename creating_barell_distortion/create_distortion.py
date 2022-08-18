
from wand.image import Image
import numpy as np
import cv2


with Image(filename='image004.jpg') as img:
    print(img.size)
    img.virtual_pixel = 'transparent'
    img.distort('barrel', (0.1, 0.0, 0.0, 1.0))
    img.save(filename='checks_barrel.png')
    # convert to opencv/numpy array format
    img_opencv = np.array(img)

# display result with opencv
#cv2.imshow("BARREL", img_opencv)
#cv2.waitKey(0)
cv2.destroyAllWindows()
