import freenect
import cv2

def get_video():
    array, _ = freenect.sync_get_video()
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return array

def set_path(namePic):
    setPath = '/home/uawsscu/PycharmProjects/Project2/image/' + namePic + '.jpg'
    return setPath

def cap_ture(pathPic):
    setPath = '/home/uawsscu/PycharmProjects/Project2/image/' + pathPic + '.jpg'
    while 1:
        print "ok cap_ture"
        frame = get_video()
        cv2.imshow('RGB image', frame)

        params = list()
        crop_img = frame[120:420, 213:456]  # Crop from x, y, w, h -> 100, 200, 300, 400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        cv2.imwrite(setPath, crop_img, params)

        break

    cv2.destroyAllWindows()

#cap_ture('messigray')