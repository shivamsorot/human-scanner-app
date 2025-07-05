from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO('yolov8n.pt')

# Check if OpenCV GUI functions are available
def is_cv2_gui_available():
    try:
        cv2.namedWindow('test')
        cv2.destroyWindow('test')
        return True
    except cv2.error:
        return False

cv2_gui_available = is_cv2_gui_available()

# Open the video capture for live stream (webcam)
cap = cv2.VideoCapture(0)
address = "https://192.168.31.127:8080/video"
cap.open(address)

# Check if the webcam was opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    # Initialize frame read success flag
    ret = True

    while ret:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame was successfully read
        if not ret or frame is None:
            break

        # Ensure the frame is consistently sized
        frame = cv2.resize(frame, (640, 480))

        try:
            # Perform object tracking
            results = model.track(frame, persist=True)

            # Plot the results on the frame
            frame_ = results[0].plot()

            # Display the frame with bounding boxes if GUI support is available
            if cv2_gui_available:
                cv2.imshow('frame', frame_)
                # Break the loop if 'q' is pressed
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

        except cv2.error as e:
            print(f"OpenCV error: {e}")
            break

    # Release the video capture
    cap.release()

# Close all OpenCV windows if GUI support is available
if cv2_gui_available:
    cv2.destroyAllWindows()
    