import cv2
import pytesseract

def detector(file):

    # Mention the installed location of Tesseract-OCR in your system. I use a mac, so it will most probably be compatible with other Mac OS devices
    pytesseract.pytesseract.tesseract_cmd = '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages'

    # Reading the ad
    img = cv2.imread(file)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting to grayscale


    ret, thresh1 = cv2.threshold(
        gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))


    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)


    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_NONE)


    im2 = img.copy()


    file = open("recognized.txt", "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped = im2[y:y + h, x:x + w]

        file = open("recognized.txt", "a")

        text = pytesseract.image_to_string(cropped)

        file.write(text)
        file.write("\n")

        file.close
