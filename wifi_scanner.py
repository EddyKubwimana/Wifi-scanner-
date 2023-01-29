#Wifi scanner on a laptop
import cv2
from pyzbar.pyzbar import decode
import os

vid = cv2.VideoCapture(0)
while True:
    _,img = vid.read(0)
    db = decode(img)
    for data in db:
        try:
            new =data.data.decode("utf-8").split(":")
            d,*_ = new[2].split(";")
            password,*_= new[4].split(";")
            print(d,password)
            
            os.system(f'cmd/c "netsh wlan hostednetwork mode = allow ssid = {d} key = {password}"')
            os.system(f'cmd/c "netsh wlan connect ssid = {d} name= {d}"')
        except:
            pass
    cv2.imshow("result",img)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break
cv2.destroyWindow('result')
        
    
