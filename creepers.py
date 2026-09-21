import cv2
import numpy as np


class ProcessImage:
    def __init__(self):
        self.bgr = None
        self.hsv = None
        self.mask_green = None
        self.mask_blue = None
        self.mask_red = None
        self.mask = None

    def run_image(self, image):
        self.bgr = image
        self.hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)

        lower_green = np.array([35, 50, 50])
        upper_green = np.array([85, 255, 255])
        self.mask_green = cv2.inRange(self.hsv, lower_green, upper_green)

        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        self.mask_blue = cv2.inRange(self.hsv, lower_blue, upper_blue)

        
        lower_red_1 = np.array([0, 50, 50])
        upper_red_1 = np.array([10, 255, 255])
        lower_red_2 = np.array([170, 50, 50])
        upper_red_2 = np.array([180, 255, 255])

        mask_red_1 = cv2.inRange(self.hsv, lower_red_1, upper_red_1)
        mask_red_2 = cv2.inRange(self.hsv, lower_red_2, upper_red_2)
        self.mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

        self.mask = cv2.add(self.mask_green, self.mask_blue)
        self.mask = cv2.add(self.mask, self.mask_red)

    def show_image(self):
        cv2.imshow("Imagem original", self.bgr)
        cv2.imshow("Mascara", self.mask)


def main():
    process_image = ProcessImage()

    webcam = cv2.VideoCapture(0)

    while True:
        val, image = webcam.read()

        if val:
            process_image.run_image(image)
            process_image.show_image()

        if cv2.waitKey(1) == 27:  
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
