import cv2 
import matplotlib.pyplot as plt
import time
################################CAPTURING IMAGE 5 TIMES FROM THE WEBCAM #################################


i = 0
image_list = []
while(i<5):
	cap = cv2.VideoCapture(0)
	if (cap.isOpened()):
		ret,frame = cap.read()
		print(ret)
	else:
		ret = False
	img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	image_list.append(img)
	i+=1
	time.sleep(5)
	cap.release()

i = 4
while(i>=0):
	print(i)
	plt.imshow(image_list[i])
	plt.show()
	i-=1
#########################################################################################################