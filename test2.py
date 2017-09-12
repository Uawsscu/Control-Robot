import freenect
import cv2
import numpy as np


# function to get RGB image from kinect
def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array


# function to get depth image from kinect
def get_depth():
    array, _ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array


if __name__ == "__main__":
    while 1:
        print "ok"
        # get a frame from RGB camera
        frame = get_video()
        # get a frame from depth sensor

        # display RGB image
        cv2.imshow('RGB image', frame)
        # display depth image



        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        params = list()

        params.append(8)
        cv2.imwrite('/home/uawsscu/PycharmProjects/Project2/messigray.jpg', frame, params)

        break
        if k == 27:
            break
    cv2.destroyAllWindows()