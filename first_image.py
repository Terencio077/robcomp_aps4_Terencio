import cv2
class ProcessImage():
    def __init__(self):
        self.bgr = None

    def load_image(self, image_path):
        self.bgr = cv2.imread(image_path)

    def show_image(self):

        cv2.imshow("Imagem", self.bgr)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def show_channels(self):
        blue, green, red = cv2.split(self.bgr)
        cv2.imshow("Canal B", blue)
        cv2.imshow("Canal G", green)
        cv2.imshow("Canal R", red)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    processor = ProcessImage()
    processor.load_image("img/arara.jpg")

    processor.show_channels()

if __name__ == "__main__":
    main()


    
