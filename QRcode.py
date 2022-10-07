import qrcode
import cv2
Name = input("Name : ")
age = input("Age : ")
img = qrcode.make("Name : " + Name + "\nAge : " + age)
img.save('qrcode.jpg')
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
