import pyzbar
import cv2
from imutils import rotate_bound


class BarcodeReader:
    def __init__(self):
        self.type_barcode = None
        self.data_barcode = None

    def decode(self, img):
        """
        Decodes the barcode in the given image
        """
        decoded_objects = pyzbar.decode(img)

        if not decoded_objects:
            return None, None, None

        for obj in decoded_objects:
            print("barcode detected:", obj)
            img = self._draw_barcode(obj, img)
            self.type_barcode = obj.type
            self.data_barcode = obj.data.decode('utf-8')

        return img, self.type_barcode, self.data_barcode

    def _draw_barcode(self, decoded, img):
        """
        Draws a rectangle around the barcode
        """
        img = cv2.rectangle(
            img,
            (decoded.rect.left, decoded.rect.top),
            (decoded.rect.left + decoded.rect.width,
             decoded.rect.top + decoded.rect.height),
            color=(0, 255, 0),
            thickness=5
        )

        return img

    def read_barcode(self, img):
        """
        Checks the rotations of the image until it finds the barcode
        """
        img_copy = img.copy()
        img_ = None
        step = 5  # 5° rotation
        i = 1  # rotates up to 180°
        while img_ is None and i < 180:
            img_, self.type_barcode, self.data_barcode = self.decode(img_copy)
            if self.data_barcode:
                break
            img_copy = rotate_bound(img_copy, i)
            i += step
        return img_, self.type_barcode, self.data_barcode


class Camera:
    def __init__(self):
        self.barcode_reader = BarcodeReader()
        self.camera = cv2.VideoCapture(0)

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def start(self):
        """
        Opens the camera and captures the barcode
        """
        ret, frame = self.camera.read()

        # Loop to show the image and close the tab
        while ret:
            ret, frame = self.camera.read()
            frame = self.barcode_reader._cam_decode(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

    def _cam_decode(self, frame):
        """
        Decodes the barcode in the camera frame
        """
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6),
                        font, 0.7, (255, 0, 0), 1)
        return frame
