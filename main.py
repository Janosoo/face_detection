# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import os
def print_hi(name):


    face_cascade = cv2.CascadeClassifier('face_detector.xml')

    files = os.listdir()

    for file in files:
        if '.jp' in file:


            img = cv2.imread(file)

            faces = face_cascade.detectMultiScale(img, 1.1, 4)
            print(file)*
            print(faces)

            if faces != ():

                # Draw rectangle around the faces
                for (x, y, w, h) in faces:

                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                cv2.imwrite(file[:-4] +"face_detected2.png", img)
                print('Successfully saved')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
