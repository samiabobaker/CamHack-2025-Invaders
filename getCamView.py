# screen = np.asarray(Image.open("../Unknown.png").convert('RGB'))
# print(screen.shape)

# clipped_screen = screen[131:131+186, 1509:1509+331]
# new_im = Image.fromarray(clipped_screen)
# new_im.show()

# clipped_screen = screen[331:331+186, 1509:1509+331]
# new_im = Image.fromarray(clipped_screen)
# new_im.show()

# clipped_screen = screen[532:532+186, 1509:1509+331]
# new_im = Image.fromarray(clipped_screen)
# new_im.show()

# clipped_screen = screen[734:734+186, 1509:1509+331]
# new_im = Image.fromarray(clipped_screen)
# new_im.show()

import cv2
import numpy as np

# load image
image = cv2.imread("../Unknown.png")

def get_players_from_screenshot(image):
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur image
    blur = cv2.medianBlur(gray, 5)

    # Sharpen image by kernelling
    sharpen_kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    # threshold
    thresh = cv2.threshold(sharpen, 20, 255, cv2.THRESH_BINARY)[1]

    # apply close morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # get largest contour and draw on copy of input
    result = image.copy()
    contours = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    cv2.drawContours(result, contours, 0, (255,255,255), 1)

    min_area = 600000
    max_area = 800000
    image_number = 0

    images = []

    for c in contours:
        area = cv2.contourArea(c)
        if area > min_area and area < max_area:
            x,y,w,h = cv2.boundingRect(c)

            images.append((x,y,w,h))

            #ROI = image[y:y+h, x:x+w]

            #images.append(cv2.resize(ROI, dsize=(100,100)))
            #key = cv2.waitKey(20)
            #if key == 27: # exit on ESC
            #    break

            # Commands below are unnecessary
            #cv2.imwrite('log/ROI_{}.png'.format(image_number), ROI)
            #cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
            #image_number += 1
    
    return images

