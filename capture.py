import cv2

def capture():
    cap = cv2.VideoCapture(0)
    count = 0

    while(True):
        # フレームをキャプチャする
        ret, frame = cap.read()

        if count == 3:
            path = "photo/photo.jpg"
            cv2.imwrite(path,frame)
            break

        count += 1



    # キャプチャの後始末と，ウィンドウをすべて消す
    cap.release()
    cv2.destroyAllWindows()
