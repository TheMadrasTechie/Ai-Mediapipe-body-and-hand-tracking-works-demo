import cv2


def main():
    
    # reading the input
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter('output.mp4', fourcc, 24, (640, 480))

    while(True):
        ret, frame = cap.read()
        if(ret):
            
            # adding rectangle on each frame
            cv2.rectangle(frame, (100, 100), (500, 500), (0, 255, 0), 3)
            
            # writing the new frame in output
            output.write(frame)
            cv2.imshow("output", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break

    cv2.destroyAllWindows()
    output.release()
    cap.release()


if __name__ == "__main__":
    main()