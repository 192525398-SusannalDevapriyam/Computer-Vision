import cv2

cap = cv2.VideoCapture(r"C:\Users\lenin\Videos\Screen Recordings\lu.mp4")

if not cap.isOpened():
    print("Video not found!")
else:
    print("Press:")
    print("N - Normal Speed")
    print("S - Slow Motion")
    print("F - Fast Motion")
    print("Q - Quit")

    speed = 30

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        key = cv2.waitKey(speed) & 0xFF

        if key == ord('s'):
            speed = 100
        elif key == ord('f'):
            speed = 5
        elif key == ord('n'):
            speed = 30
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
