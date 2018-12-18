import math
import numpy as np
import cv2
def shapedetector():
            list=[]
            #dictionary of all contours
            contours = {}
            #array of edges of polygon
            approx = []
            #scale of the text
            scale = 2
            #camera
            cap = cv2.VideoCapture(0)
            print("press ESC to exit")

            
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

            #calculate angle
            def angle(pt1,pt2,pt0):
                dx1 = pt1[0][0] - pt0[0][0]
                dy1 = pt1[0][1] - pt0[0][1]
                dx2 = pt2[0][0] - pt0[0][0]
                dy2 = pt2[0][1] - pt0[0][1]
                return float((dx1*dx2 + dy1*dy2))/math.sqrt(float((dx1*dx1 + dy1*dy1))*(dx2*dx2 + dy2*dy2) + 1e-10)

            while(cap.isOpened()):
                #Capture frame-by-frame
                ret, frame = cap.read()
                if ret==True:
                    #grayscale
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    #Canny
                    canny = cv2.Canny(frame,80,240,3)

                    #contours
                    canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                    for i in range(0,len(contours)):
                        #approximate the contour with accuracy proportional to
                        #the contour perimeter
                        approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.02,True)
                        
                        # to draw contours     
                        cv2.drawContours(frame, contours[i], -1, (0, 0 ,255), 3)
            
                        #Skip small or non-convex objects
                        if(abs(cv2.contourArea(contours[i]))<100 or not(cv2.isContourConvex(approx))):
                            continue

                        #triangle
                        if(len(approx) == 3):
                            x,y,w,h = cv2.boundingRect(contours[i])
                            cv2.putText(frame,'TRIANGLE',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
                            list.append("triangle")
                        elif(len(approx)>=4 and len(approx)<=6):
                            #nb vertices of a polygonal curve
                            vtc = len(approx)
                            '''#get cos of all corners
                            cos = []
                            for j in range(2,vtc+1):
                                cos.append(angle(approx[j%vtc],approx[j-2],approx[j-1]))'''

                            
                            #to determine the shape of the contour
                            x,y,w,h = cv2.boundingRect(contours[i])
                            if(vtc==4):
                                cv2.putText(frame,'RECTANGLE',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
                                list.append("rectangle")
                            elif(vtc==5):
                                cv2.putText(frame,'PENTAGON',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
                                list.append("pentagon")
                            elif(vtc==6):
                                cv2.putText(frame,'HEXA',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
                                list.append("HEXAGAN")
                        else:
                            #detect and label circle
                            area = cv2.contourArea(contours[i])
                            x,y,w,h = cv2.boundingRect(contours[i])
                            radius = w/2
                            if(abs(1 - (float(w)/h))<=2 and abs(1-(area/(math.pi*radius*radius)))<=0.2):
                                cv2.putText(frame,'CIRCLE',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
                                list.append("circle")
                    #Display the resulting frame
                    out.write(frame)
                    cv2.imshow('frame',frame)
                    cv2.imshow('canny',canny)
                    if cv2.waitKey(1) == 27: #if ESC is pressed
                        break

            #When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
            return list[-1]
      
ans=shapedetector()


# Brother its mine code dont dare to touch it 
import webbrowser as browser
string = ans
if (string == "triangle"):
	browser.open("triangle.html")
elif (string == "rectangle"):
	browser.open("rectangle.html")
elif (string == "circle"):
	browser.open("circle.html")
elif(string=="pentagon"):
	browser.open("pentagon.html")
else:
	print("The shape is not defined")



