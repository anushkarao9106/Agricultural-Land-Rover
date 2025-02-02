# Agricultural-land-rover
import cv2 #opencv
import urllib.request #para abrir y leer URL
import numpy as np
from capture import ProcessImage
#PROGRAMA DE CLASIFICACION DE OBJETOS PARA VIDEO EN DIRECCION IP 

url = 'http://192.168.100.13/cam-hi.jpg'
#url = 'http://192.168.1.77/cam-hi.jpg'
#url = 'http://192.168.1.11/'
winName = 'ESP32 CAMERA'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
#scale_percent = 80 # percent of original size    #para procesamiento de imagen


import time
while(1):
    imgResponse = urllib.request.urlopen (url) #abrimos el URL
    imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img = cv2.imdecode (imgNp,-1) #decodificamos

    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # vertical
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #black and white

    

    Disease,per=ProcessImage(img)
    cv2.imshow("Predicted Output", Disease)

    if (per>75): 
        print('Given Leaf Image is Dieseased Level 3 with '+str(per)+' %')
        
        time.sleep(0.5)
      
        
    elif (per>40) and (per<75):
        print('Given Leaf Image is Dieseased Level 2 with '+str(per)+' %')
        
        time.sleep(0.5)
       
    
    elif (per<40) and (per>25):
        print('Given Leaf Image is Dieseased Level 1 with '+str(per)+' %')

        time.sleep(0.5)
        
    else:
        print('Given Leaf Image is Good')
        
        time.sleep(0.5)
    time.sleep(.1)
   


    cv2.imshow(winName,img) # mostramos la imagen

    #esperamos a que se presione ESC para terminar el programa
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()
