import cv2

def capture():
    cap = cv2.VideoCapture(0)
    count = 0

    while(True):
        ret, frame = cap.read()

        if count == 3:
            path = "photo/photo.jpg"
            cv2.imwrite(path,frame)
            break

        count += 1



    cap.release()
    cv2.destroyAllWindows()
