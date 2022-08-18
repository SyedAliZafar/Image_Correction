# Image_Correction


# Barrell Distortion 

Barrel distortion is a loss of resolution in an image that results from the camera's lens being at its focal length. When you take a picture, your camera creates an image by stretching digital information (like colors) to create pixels that are larger on the periphery and smaller in the center. 
This can make objects look distorted because they "melt" into each other when viewed up-close or from certain angles.
-What is the difference between pincushion and barreled distortion? 

-

Pincushion distortion is a less harmful type of barrel distortion that occurs when the camera lens tries to make the image look rounder and tighter. Barreled distortion, on the other hand, can cause images to appear as if they are swollen or distorted along one dimension.

## Remove distortion 


*Step1: it gets the values that could be used as a distortion coeefficient for correcting the image

$python test.py 


Directory:> [D:\image_processing\Image_Manipulation_Correctness\camera-correction]
	
* Step2: This program should be tried for correctness
[D:\image_processing\Image_Manipulation_Correctness\correcting_distortion\lenpyprogram.ipynb]

* Step3: Use the coeefficient values from Step1 and put the values in 

### TODO: add your coefficients here!
k1 = -6.3100000000000006e-05; # negative to remove barrel distortion
k2 = 0;
p1 = 0;
p2 = 0


Step4: Caluclate pixel
