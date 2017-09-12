import freenect
import cv2
import numpy as np


# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

def set_path(namePic):
    setPath = '/home/uawsscu/PycharmProjects/Project2/' + namePic + '.jpg'
    return setPath

def cap_ture(pathPic):
    while 1:
        print "ok"
        frame = get_video()
        cv2.imshow('RGB image', frame)
        k = cv2.waitKey(5) & 0xFF
        params = list()

        params.append(8)
        cv2.imwrite(set_path(pathPic), frame, params)

        break
        if k == 27:
            break
    cv2.destroyAllWindows()

cap_ture('messigray')