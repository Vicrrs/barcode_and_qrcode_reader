import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
from pyzbar import pyzbar

img = cv2.imread(
    "imgs/bar15.jpeg")  # if use cv2

# specify code type
codes = pyzbar.decode(img)  # auto detect code type
print('Decoded:', codes)

for code in codes:
    data = code.data.decode('ascii')
    print('Data:', code.data.decode('ascii'))
    print('Code Type:', code.type)
    print('BBox:', code.rect)
    x, y, w, h = code.rect.left, code.rect.top, \
        code.rect.width, code.rect.height
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 8)
    print('Polygon:', code.polygon)
    cv2.rectangle(img, code.polygon[0], code.polygon[1],
                  (0, 255, 0), 4)

    txt = '(' + code.type + ')  ' + data
    cv2.putText(img, txt, (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)

text1 = (f"No. Codes: {len(codes)}")
cv2.putText(img, text1, (5, 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


cv2.imshow('bounding box', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
