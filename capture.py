# this piece of code click images every second
# captured images can be used to train the model by cutting and pasting the desired class folder

#importing libraries
import cv2
import time

def capture_photos(output_folder):
    # Open the default camera (0)

    pathToVideoFile = r"C:\Users\abhis\Videos\2024-05-28_09-50-40.mkv"
    cap = cv2.VideoCapture(pathToVideoFile)


    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):        #creating folder to save pictures in
        os.makedirs(output_folder)

    photo_count = 0

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Couldn't capture frame.")
                break

            # Save the captured frame to a file
            photo_filename = f"{output_folder}/photo_{photo_count + 1}.jpg"
            cv2.imwrite(photo_filename, frame)        # saving pictures

            print(f"Photo {photo_count + 1} captured: {photo_filename}")

            photo_count += 1

    except KeyboardInterrupt:
        print("Capturing interrupted by user.")
    finally:
        # Release the camera when done
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import os

    output_folder = "captured_photos"
    capture_photos(output_folder)
