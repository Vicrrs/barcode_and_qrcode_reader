import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
from pyzbar import pyzbar

img = cv2.imread(
    "imgs/bar1.jpeg", 2)  # if use cv2

# specify code type
codes = pyzbar.decode(img)  # auto detect code type
print('Decoded:', codes)

if len(codes) == 0:
    imgr = cv2. rotate(img, rotateCode=2)

    h, w = img.shape
    center = (h//2, w//2)

    rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.85)
    final_rotated = cv2.warpAffine(img, rotation_matrix, (w, h))

    for code in codes:
        data = code.data.decode('ascii')
        print('Data:', code.data.decode('ascii'))
        print('Code Type:', code.type)
        print('BBox:', code.rect)
        x, y, w, h = code.rect.left, code.rect.top, \
            code.rect.width, code.rect.height
        cv2.rectangle(final_rotated, (x, y), (x+w, y+h), (255, 0, 0), 8)
        print('Polygon:', code.polygon)
        cv2.rectangle(final_rotated, code.polygon[0], code.polygon[1],
                    (0, 255, 0), 4)

        txt = '(' + code.type + ')  ' + data
        cv2.putText(final_rotated, txt, (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

    text1 = (f"No. Codes: {len(codes)}")
    cv2.putText(final_rotated, text1, (5, 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


cv2.imshow('bounding box', final_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
