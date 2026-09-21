import cv2


class ProcessImage:

    def __init__(self):
        self.bgr = None
        self.rgb = None
        self.transposta = None

    def run_image(self, image):
        self.bgr = image
        self.rgb = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2RGB)
        self.transposta = self.rgb.transpose((1, 0, 2))

    def show_image(self):
        cv2.imshow("cam", self.transposta)


def main():
    process_image = ProcessImage()

    webcam = cv2.VideoCapture(0)
    cv2.namedWindow("cam")

    while True:
        val, image = webcam.read()

        if val:
            process_image.run_image(image)
            process_image.show_image()

        if cv2.waitKey(1) == 27:  # Aguarda 1 ms pela tecla Esc
            break

    cv2.destroyAllWindows()
    webcam.release()


if __name__ == "__main__":
    main()