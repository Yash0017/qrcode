import cv2

read = cv2.QRCodeDetector()
value, points, _ = read.detectAndDecode(cv2.imread("qrcode.jpg"))
print(points)

