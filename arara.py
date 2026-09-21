import cv2


class ProcessImage:
    def __init__(self):
        self.bgr = None

    def run_image(self, image):
        self.bgr = image.copy()

        height, width, channels = self.bgr.shape

        half_height = int(height / 2)
        one_third_width = int(width / 3)
        two_thirds_width = int(2 * width / 3)

        
        self.bgr[:half_height, one_third_width:two_thirds_width] = 0

        self.bgr[half_height:, :one_third_width] = 0
        self.bgr[half_height:, two_thirds_width:] = 0

    def show_image(self):
        cv2.imshow("Arara", self.bgr)
        cv2.waitKey()
        cv2.destroyAllWindows()


def main():
    process_image = ProcessImage()
    image = cv2.imread("img/arara.jpg")
    process_image.run_image(image)
    process_image.show_image()


if __name__ == "__main__":
    main()
