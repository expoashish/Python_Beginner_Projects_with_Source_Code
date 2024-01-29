import cv2 #pip install opencv-python


def remove_green_background(image):
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_green = (50,100,100)
    upper_green = (100,255,255)
    mask = cv2.inRange(hsv,lower_green,upper_green)
    mask = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(image,image, mask=mask)
    cv2.imwrite("output1.png",result)
    return result

if __name__=="__main__":
    image = cv2.imread("green2.jpg")
    result = remove_green_background(image)
    cv2.imshow("Result=",result)
    cv2.waitKey(0)