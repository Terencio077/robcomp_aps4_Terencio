import cv2


class ProcessImage:
    def __init__(self):
        self.bgr = None
        self.gray = None

    def run_image(self, image):
        self.bgr = image
        self.gray = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2GRAY)

        self.gray[self.gray < 128] = 0
        self.gray[self.gray >= 128] = 255

    def show_image(self):
        cv2.imshow("Webcam BW", self.gray)


def main():
    process_image = ProcessImage()

    webcam = cv2.VideoCapture(0)
    cv2.namedWindow("Webcam BW")

    while True:
        val, image = webcam.read()

        if val:
            process_image.run_image(image)
            process_image.show_image()

        if cv2.waitKey(1) == 27:  # Tecla Esc
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
