import  cv2
import matplotlib.pyplot as plt
import numpy as np
gray = cv2.imread("img.jpeg")
#print(len(image))
image = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
#plt.imshow(image)
li =[
		 [ 1 , 0 , -1 ],
		 [ 1 , 0 , -1 ],
		 [ 1 , 0 , -1 ]


	]
img = np.array(image)
ker = np.array(li)


def convolution2d(image, kernel, bias):
	m, n = kernel.shape
	if (m == n):
		y, x = image.shape
		y = y - m + 1
		x = x - m + 1
		new_image = np.zeros((y,x))
		for i in range(y):
			for j in range(x):
				new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
	return new_image
newimg = convolution2d(img,ker,2)
plt.imshow(newimg)
plt.show()
