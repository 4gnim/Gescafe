import os
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("Resources/Background.png")

# importing all the mode images to a list
folderPathModes = "Resources/Modes"
listImgModesPath = os.listdir(folderPathModes)
listImgModes = []
for imgModePath in listImgModesPath:
    listImgModes.append(cv2.imread(os.path.join(folderPathModes, imgModePath)))

# importing all the icons to a list
folderPathIcons = "Resources/Icons"
listImgIconsPath = os.listdir(folderPathIcons)
listImgIcons = []
for imgIconsPath in listImgIconsPath:
    listImgIcons.append(cv2.imread(os.path.join(folderPathIcons, imgIconsPath)))

modeType = 0  # for changing selection mode
selection = -1
counter = 0
selectionSpeed = 7
counterPause = 0
selectionList = [-1, -1, -1, -1]

detector = HandDetector(detectionCon=0.8, maxHands=1)
modePositions = [(1136, 196), (1000, 384), (1136, 581), (1000, 787)]

while True:
    success, img = cap.read()

    # Find the hand and its landmarks
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # overlaying the webcam feed on the background image
    imgBackground[139:139 + 480, 50:50 + 640] = img
    imgBackground[0:720, 847: 1280] = listImgModes[modeType]

    if hands and counterPause == 0:
        # Hand 1
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

        # Detect forward gestures
        if modeType < 4:
            if fingers1 == [0, 1, 0, 0, 0]:
                if selection != 1:
                    counter = 1
                selection = 1
            elif fingers1 == [0, 1, 1, 0, 0]:
                if selection != 2:
                    counter = 1
                selection = 2
            elif fingers1 == [0, 1, 1, 1, 0]:
                if selection != 3:
                    counter = 1
                selection = 3
            else:
                selection = -1
                counter = 0

            if counter > 0:
                counter += 1
                cv2.ellipse(imgBackground, modePositions[selection - 1], (103, 103), 0, 0,
                            counter * selectionSpeed, (0, 255, 0), 20)
                
                if counter * selectionSpeed > 360:
                    selectionList[modeType] = selection
                    modeType += 1
                    counter = 0
                    selection = -1
                    counterPause = 1

        # Detect back gesture (all fingers up)
        if fingers1 == [1, 1, 1, 1, 1] and modeType > 0:
            print("Back gesture detected!")
            modeType -= 1
            selectionList[modeType] = -1  # Remove the icon from the current mode
            counterPause = 1

    # To pause after each selection or back action
    if counterPause > 0:
        counterPause += 1
        if counterPause > 60:
            counterPause = 0

    # Add selection icon at the bottom
    if selectionList[0] != -1:
        imgBackground[636:636 + 65, 30:30 + 65] = listImgIcons[selectionList[0] - 1]
    else:
        imgBackground[636:636 + 65, 30:30 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)

    if selectionList[1] != -1:
        imgBackground[636:636 + 65, 238:238 + 65] = listImgIcons[5 + selectionList[1]]
    else:
        imgBackground[636:636 + 65, 238:238 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)

    if selectionList[2] != -1:
        imgBackground[636:636 + 65, 444:444 + 65] = listImgIcons[2 + selectionList[2]]
    else:
        imgBackground[636:636 + 65, 444:444 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)

    if selectionList[3] != -1:
        imgBackground[636:636 + 65, 651:651 + 65] = listImgIcons[5 + selectionList[3]]
    else:
        imgBackground[636:636 + 65, 651:651 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)

    # Detect key press for reset
    key = cv2.waitKey(1)
    if key == ord('n'):  # Reset if 'n' is pressed
        modeType = 0
        selection = -1
        counter = 0
        counterPause = 0
        selectionList = [-1, -1, -1, -1]
        # Clear all icons from the background
        imgBackground[636:636 + 65, 30:30 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)
        imgBackground[636:636 + 65, 238:238 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)
        imgBackground[636:636 + 65, 444:444 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)
        imgBackground[636:636 + 65, 651:651 + 65] = np.zeros((65, 65, 3), dtype=np.uint8)
        print("Reset successful!")

    # Displaying
    cv2.imshow("Background", imgBackground)
    if key == ord('q'):  # Exit if 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()
