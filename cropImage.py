import cv2
img = cv2.imread("/home/uawsscu/PycharmProjects/Project2/messigray.jpg")
crop_img = img[120:420, 213:456] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

cv2.imwrite('/home/uawsscu/PycharmProjects/Project2/c1.jpg',crop_img)
print "pass"
#x=213-456  y =150-360