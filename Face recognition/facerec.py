import cv2
from pynput.keyboard import Key, Controller
# define a video capture object
keyboard = Controller()
keyboard.press(Key.cmd)
keyboard.press('F6')
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# import face_recognition
# from PIL import Image
#
# image = face_recognition.load_image_file("test.png")
# face_locations = face_recognition.face_locations(image)
#
# for face in face_locations:
#     print(face)
#     top, right, bottom, left = face
#     output_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(output_image)
#     pil_image.show(title=f"{face}")
#
