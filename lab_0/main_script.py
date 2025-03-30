import matplotlib.pyplot as plt
from fontTools.unicodedata import block

plt.ion()
import numpy as np
from PIL import Image


# load the image
image=Image.open('data/lemon.png')

# Convert the image to a numpy array
image = np.array(image)

# Get the range of values of the image
min_value=np.min(image)
max_value=np.max(image)

print(f"Minimum value: {min_value} ")
print(f"Maximum value: {max_value} ")

# convert the image data into 0-1 range
image =image/255

# Get the range of the values of the image
min_value=np.min(image)
max_value=np.max(image)

#printing the new values
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")

#plotting the normal way
plt.imshow(image)
plt.show(block=True)  # This will block further execution until you close the window

#plotting the subplots for better control
f,ax=plt.subplots()

#display the subplot images
ax.imshow(image)

plt.show(block=True)

# display images of the different channels

r_image=image[:,:,0]

g_image=image[:,:,1]

b_image=image[:,:,2]



# plotting individual images
f_1,ax_1=plt.subplots()
ax_1.imshow(r_image)
plt.show(block=True)

f_2,ax_2=plt.subplots()
ax_2.imshow(g_image)
plt.show(block=True)

f_3,ax_3=plt.subplots()
ax_3.imshow(b_image)
plt.show(block=True)

print(image.shape)

# convert into grey scale
grey_image=np.mean(image,axis=2)

# plot the grey image
print(grey_image.shape)

f_gr,ax_gr=plt.subplots()
ax_gr.imshow(grey_image)
plt.show(block=True)

# luminous greyscale image
lum_grey_image=0.2989*image[:,:,0]+0.5870*image[:,:,1]+0.1140*image[:,:,2]

f_lgr,ax_lgr=plt.subplots()
ax_lgr.imshow(lum_grey_image)
plt.show(block=True)


