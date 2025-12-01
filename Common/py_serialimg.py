import numpy as np
import serial
import msvcrt
import cv2
import time

MCU_WRITES = 87
MCU_READS = 82
# Request Type
rqType = {MCU_WRITES: "MCU Sends Image", MCU_READS: "PC Sends Image"}

# Format
formatType = {
    1: "Grayscale",
    2: "RGB565",
    3: "RGB888",
}

IMAGE_FORMAT_GRAYSCALE = 1
IMAGE_FORMAT_RGB565 = 2
IMAGE_FORMAT_RGB888 = 3


# Init Com Port
def SERIAL_Init(port):
    global __serial
    __serial = serial.Serial(port, 2000000)
    __serial.flush()
    print(__serial.name, "Opened")
    print("")


# Wait for MCU Request
def SERIAL_IMG_PollForRequest():
    global requestType
    global height
    global width
    global format
    global imgSize
    while 1:
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            print("Exit program!")
            exit(0)
        if np.frombuffer(__serial.read(1), dtype=np.uint8) == 83:
            if np.frombuffer(__serial.read(1), dtype=np.uint8) == 84:
                requestType = int(np.frombuffer(__serial.read(1), dtype=np.uint8))
                height = int(np.frombuffer(__serial.read(2), dtype=np.uint16))
                width = int(np.frombuffer(__serial.read(2), dtype=np.uint16))
                format = int(np.frombuffer(__serial.read(1), dtype=np.uint8))
                imgSize = height * width * format

                print("Request Type : ", rqType[int(requestType)])
                print("Height       : ", int(height))
                print("Width        : ", int(width))
                print("Format       : ", formatType[int(format)])
                print()
                return [int(requestType), int(height), int(width), int(format)]


# Reads Image from MCU
def SERIAL_IMG_Read():
    img = np.frombuffer(__serial.read(imgSize), dtype=np.uint8)
    img = np.reshape(img, (height, width, format))
    if format == IMAGE_FORMAT_GRAYSCALE:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif format == IMAGE_FORMAT_RGB565:
        img = cv2.cvtColor(img, cv2.COLOR_BGR5652BGR)

    timestamp = time.strftime("%Y_%m_%d_%H%M%S", time.localtime())
    cv2.imshow("img", img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # cv2.imwrite("capture/image_"+ timestamp + ".jpg", img)
    return img


# Writes Image to MCU
def SERIAL_IMG_Write(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (width, height))
    if format == IMAGE_FORMAT_GRAYSCALE:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif format == IMAGE_FORMAT_RGB565:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGR565)

    img = img.tobytes()
    __serial.write(img)
