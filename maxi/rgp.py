import numpy as np 
import imageio.v3 as img 

image_path = "spongebob.jpg"
image = img.imread(image_path)

if len(image.shape) < 3 or image.shape [2] !=3 :
    print ("format gambar harus RGB")
    exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

image_red = np.zeros_like(image)
image_grey = np.zeros_like(image)

image_red[:,:,0] =red
grey = 0.299 * red + 0.587 * green + 0.144 * blue

image_grey[:,:,0] = grey
image_grey[:,:,1] = grey
image_grey[:,:,2] = grey

#img.imwrite("detinationgrey.jpg", image_red)
img.imwrite("destinationgrey.jpg", image_grey)

print ("proses berhasil")
print(image.shape)