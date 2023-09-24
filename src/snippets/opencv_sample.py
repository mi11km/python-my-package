import cv2


def main():
    # 分類器の読み込み
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                         'haarcascade_frontalface_default.xml')
    profile_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                                 'haarcascade_profileface.xml')

    # ウェブカメラからの入力を開始
    cap = cv2.VideoCapture(0)

    while True:
        # フレームをキャプチャ
        ret, frame = cap.read()

        # グレースケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 正面の顔認識
        faces = face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

        # 横顔の認識
        profile_faces = profile_face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)

        # 顔領域に矩形を描画（正面）
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 顔領域に矩形を描画（横顔）
        for (x, y, w, h) in profile_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 結果を表示
        cv2.imshow('Face Detection', frame)

        # 'q'キーが押されたら終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # ウェブカメラを解放し、ウィンドウを閉じる
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
