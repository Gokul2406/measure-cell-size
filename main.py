import cv2

def calculate_area(rfile, wfile, thresh):

    img = cv2.imread(rfile)

    # convert the img to greyscale
    greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #get threshold(bw) 126 was finalised after hit and trial
    ret, threshold = cv2.threshold(greyscaled, thresh, 255, cv2.THRESH_BINARY)

    #find contours acc to the threshold
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #draw contours 
    cv2.drawContours(threshold, contours, -1, (0, 255.0, 0), 3)

    #find are of contour
    area = cv2.contourArea(contours[0])

    print(area/1000000)


    #save file
    cv2.imwrite(wfile, threshold)


#pombe
calculate_area('./images/pombe.jpeg', './contours/pombe-contour.jpg', 120)
calculate_area('./images/yeast.jpg', './contours/yeast-contour.jpg', 130)

# 7e-4 cm2/pixel